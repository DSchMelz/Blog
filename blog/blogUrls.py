from django.urls import path
from .views import *

urlpatterns = [
    path("", postsList, name = "postsList_url"),#присваиваем имя, чтобы удобнее делать ссылки
    path("post/<str:slug>/", PostDetail.as_view(), name = "post_detail_url"),#ссылка будет такая: сервер/post/имя slug в бд
    path("tags/", tags_list, name = "tags_list_url"),
    path("tag/<str:slug>/", TagDetail.as_view(), name = "tag_detail_url"),
]