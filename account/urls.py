from django.urls import path, include
from account import views

urlpatterns = [
    # TODO: edit profile url and add <int:user_id> and edit another pages to work with this url
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name='profile'),
    path('profile-edit/<int:user_id>/', views.UpdateProfileView.as_view(), name='profile-edit'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('follow/', views.ProfileList.as_view(), name='profile_list'),
    path('add_follow/<int:user_id>', views.FollowProfileView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>', views.UnfollowProfileView.as_view(), name='unfollow_user'),
    path('profile_search/', views.SearchProfileView.as_view(), name='profile_search'),
    path('', include('django.contrib.auth.urls')),
]
