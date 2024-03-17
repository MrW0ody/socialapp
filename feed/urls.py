from django.urls import path
from feed import views

app_name = 'feed'

urlpatterns = [
    # posts urls
    path('list_posts/<int:id>/', views.PostListView.as_view(), name='list_posts'),
    path('detail_post/<int:post_id>/', views.PostDetailView.as_view(), name='detail_post'),
    path('add_post/', views.PostCreateView.as_view(), name='add_post'),
    path('delete_post/<int:post_id>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('update_post/<int:post_id>/', views.PostUpdateView.as_view(), name='update_post'),
    path('react_to_post/<int:post_id>/', views.ReactToPost.as_view(), name='react_to_post'),
    path('react_to_comment/<int:comment_id>/', views.ReactToComment.as_view(), name='react_to_comment'),
    path('search_posts/', views.SearchPostView.as_view(), name='search_posts'),

    # comment urls
    path('add_comment/<int:post_id>', views.CreateCommentView.as_view(), name='add_comment'),
    path('update_comment/<int:comment_id>', views.UpdateCommentView.as_view(), name='update_comment'),
    path('delete_comment/<int:comment_id>', views.DeleteCommentView.as_view(), name='delete_comment'),
]
