from django.urls import path
from .views import *

urlpatterns = [
    path("", postsList, name = "postsList_url"),#присваиваем имя, чтобы удобнее делать ссылки
    path("post/create/", PostCreate.as_view(), name = "post_create_url"),
    path("post/<str:slug>/", PostDetail.as_view(), name = "post_detail_url"),#ссылка будет такая: сервер/post/имя slug в бд
    path("post/<str:slug>/update", PostUpdate.as_view(), name="post_update_url"),
    path("tags/", tags_list, name = "tags_list_url"),
    path("tag/create/", TagCreate.as_view(), name = "tag_create_url"),
    path("tag/<str:slug>/", TagDetail.as_view(), name = "tag_detail_url"),
    path("tag/<str:slug>/update/", TagUpdate.as_view(), name = "tag_update_url"),
    path("tag/<str:slug>/delete/", TagDelete.as_view(), name="tag_delete_url"),
    path("post/<str:slug>/delete/", PostDelete.as_view(), name="post_delete_url")
]