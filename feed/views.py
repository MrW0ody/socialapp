from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView, CreateView, DetailView, View
from feed.models import Post, Comment
from feed.forms import PostForm, CommentForm
from django.http import Http404


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'feed/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        author = User.objects.get(id=self.kwargs['id'])
        return Post.objects.all().filter(author=author)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'feed/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post: Post = get_object_or_404(Post, pk=self.kwargs.get(self.pk_url_kwarg))
        comments: Comment = post.comments.all()
        context['comments'] = comments
        # this allows us to render form to add comment under post
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'feed/post_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('feed:list_posts', kwargs={'id': self.request.user.id})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'post_id'

    def test_func(self) -> bool:
        """
        This method specifies a condition to see if the user is authorized to see this view
        """
        post: Post = self.get_object()
        return self.request.user == post.author

    def get_object(self, queryset=None) -> Post:
        """
        This method overrides the default get_object method to check whether the logged in user is actually the author of this post
        """
        post: Post = super().get_object(queryset)
        if not post.author == self.request.user:
            raise Http404("You are not allowed to delete this post")
        return post

    def get_success_url(self) -> str:
        return reverse_lazy('feed:list_posts', kwargs={'id': self.request.user.id})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'feed/post_update.html'
    pk_url_kwarg = 'post_id'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool:
        """
        This method specifies a condition to see if the user is authorized to see this view
        """
        post: Post = self.get_object()
        return self.request.user == post.author

    def get_object(self, queryset=None) -> Post:
        """
        This method overrides the default get_object method to check whether the logged in user is actually the author of this post
        """
        post: Post = super().get_object(queryset)
        if not post.author == self.request.user:
            raise Http404("You are not allowed to edit this post")
        return post

    def get_success_url(self) -> str:
        return reverse_lazy('feed:list_posts', kwargs={'id': self.request.user.id})


class ReactToPost(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs['post_id'])
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('feed:detail_post', post_id=post.id)


class SearchPostView(LoginRequiredMixin, View):
    template_name = 'feed/post_search.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        searched_posts = Post.objects.filter(title__contains=request.POST['title'])
        return render(request, self.template_name, {'searched_posts': searched_posts})


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'feed/post_detail.html'
    pk_url_kwarg = 'post_id'

    def form_valid(self, form):
        form.instance.posts = get_object_or_404(Post, pk=self.kwargs.get(self.pk_url_kwarg))
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('feed:detail_post', kwargs={'post_id': self.kwargs.get(self.pk_url_kwarg)})


class UpdateCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'feed/comment_update.html'
    pk_url_kwarg = 'comment_id'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.object.posts_id
        return reverse_lazy('feed:detail_post', kwargs={'post_id': post_id})


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        # posts is related_name in models.py
        post_id = self.object.posts_id
        return reverse_lazy('feed:detail_post', kwargs={'post_id': post_id})


class ReactToComment(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['comment_id'])
        if comment.likes.filter(id=request.user.id):
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        return redirect('feed:detail_post', post_id=comment.posts.id)
