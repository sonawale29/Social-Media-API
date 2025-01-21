from django.urls import path
from .views import RegisterView,UserListView,UserProfileView,PostListView,PostDetailView,LikePostView,CommentPostView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/comments/', CommentPostView.as_view(), name='add_comment'),

]