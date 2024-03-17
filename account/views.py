from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView, CreateView, UpdateView, FormView
from account.forms import RegistrationForm, ProfileUpdateForm, UserUpdateForm
from account.models import Profile
from feed.models import Post, Comment


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'account/home.html'
    context_object_name = 'followed_user_posts'

    def get_queryset(self):
        current_user = self.request.user
        followed_profiles = current_user.profile.follows.all()
        print(followed_profiles)
        followed_user_posts = Post.objects.filter(author__profile__in=followed_profiles)
        print(followed_user_posts)
        return followed_user_posts


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'account/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username'].lower()
            user.email = form.cleaned_data['email'].lower()
            user.set_password(form.cleaned_data['password2'])
            user.is_active = True
            user.save()
            Profile.objects.create(user=user)
            # messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('home')
        else:
            # messages.error(request, 'Your form is invalid.')
            return render(request, 'account/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/profile.html'
    pk_url_kwarg = 'user_id'


class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'account/profile_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        logged_profile = self.request.user.profile
        profiles = Profile.objects.exclude(followed_by=logged_profile).exclude(user=self.request.user)
        return profiles


class UpdateProfileView(LoginRequiredMixin, View):
    template_name = 'account/profile_edit.html'
    pk_url_kwarg = 'user_id'

    def get(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=self.request.user)
        profile_form = ProfileUpdateForm(instance=self.request.user.profile)
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=self.request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=self.request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', user_id=request.user.id)


class FollowProfileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=self.kwargs['user_id'])
        request.user.profile.follows.add(profile)
        return redirect('profile_list')


class UnfollowProfileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=self.kwargs['user_id'])
        request.user.profile.follows.remove(profile)
        return redirect('profile', user_id=request.user.profile.id)


class SearchProfileView(LoginRequiredMixin, View):
    template_name = 'account/profile_search.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        search_profiles = User.objects.filter(username__contains=request.POST['username']).exclude(id=1)
        return render(request, self.template_name, {'search_profiles': search_profiles})
