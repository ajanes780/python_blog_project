from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,  name="index"),
    path("posts", views.posts, name="all-posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]
