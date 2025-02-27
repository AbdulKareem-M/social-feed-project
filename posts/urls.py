from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
]
