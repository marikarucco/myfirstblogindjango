from django.urls import path
from .views import (BlogCreateView, PostCreateView, PostListView, PostDeleteView, PostInsideView, CommentCreateView,
                    CommentListView)

urlpatterns = [
    path("create_blog/", BlogCreateView.as_view(), name="create_blog"),
    path("create_blog/create_post/", PostCreateView.as_view(), name="create_post"),
    path("post_list/", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostInsideView.as_view(), name="inside_post"),
    path("<int:pk>/delete_post", PostDeleteView.as_view(), name="delete_post"),
    path("<int:pk>/inside_post/create_comment/", CommentCreateView.as_view(), name="create_comment"),
    path("<int:pk>/inside_post/comment_list/", CommentListView.as_view(), name="comment_list"),

]