from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .mixins import *
from .forms import TagForm, PostForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import json

# Create your views here.
# def redirectDef(request):
#     return redirect("blog/")
#если переходим по ссылке хоста, то нас перенаправляет в "blog/"
#прозе сделать это в views, который в firstproject/firstproject, а не в firstproject/blog

def aboutList(request):
    return render(request, "blog/about.html")

def postsList(request):
    search_query = request.GET.get("search", "")#по ум = "", а не пустой = инпуту формы с именем как имя первого аргумента

    if search_query:#если поисковой запрос не пустой
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        #ищем по загловку, который содержит title or body
        #используем класс Q, чтобы можно было искать и по тайтлу, и по бади. если без него но с запятой, то будет как-будто у нас стоит and 
    else:
        posts = Post.objects.all()#печатаем все посты из бд
    #вкл шаблон хтмл

    paginator = Paginator(posts, 3)# по 3 поста на стр
    page_number = request.GET.get("page", 1)#1-значение,если не найдена стр
    page = paginator.get_page(page_number)#1 стр#это как на сайтах встречается ?параметр =

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = "?page={}".format(page.previous_page_number())
    else:
        prev_url = ""
    if page.has_next():
        next_url = "?page={}".format(page.next_page_number())
    else:
        next_url = ""

    context = {
        "page_object": page,
        "is_paginated": is_paginated,
        "next_url": next_url,
        "prev_url": prev_url
    }

    return render(request, "blog/posts.html", context = context)
    #на странице выбираем показывать при обр к posts показываем посты на этой стр
    #django будет искать шаблон в папке blog/templates/blog, поэтому указывать blog/templates не нужно

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "blog/post_detail.html"

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "blog/tag_detail.html"

def tags_list(request):
    tags = Tag.objects.all()#получаем все теги
    return render(request, "blog/tags_list.html", context = {"tags": tags})
# class TestView(View):
#     @staticmethod
#     def get(request):
#         # Здесь Вы обрабатываете запрос и формируете ответ
#         data = {
#             'time': datetime.now(),
#         }

#         return JsonResponse(data)

#     @staticmethod
#     def post(request):
#         # Здесь Вы обрабатываете запрос и формируете ответ
#         data = {
#             'post': "It is post!",
#             'comment': "It's response to POST request",
#         }

#         return JsonResponse(data)