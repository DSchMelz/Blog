from django.http import HttpResponse
from django.shortcuts import redirect

def redirectBlog(request):
   return redirect("postsList_url", permanent=True)

# def hello(request):
#    return HttpResponse("<h1>Hello world</h1>")#выводим заголовок h1