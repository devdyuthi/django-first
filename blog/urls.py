from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="start"),
    path("posts", views.posts, name="view_post"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail")
]
