from .models import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

class ObjectDetailMixin:#испотуем миксины
    model = None
    template = None
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact = slug)#чтобы если не найден выводилось 404
        return render(request, self.template, context = {self.model.__name__.lower(): obj, "admin_obj": obj, "detail": True})
        # send_mail(
        #     'Новый пост',
        #     'Вышел новый пост! Заходите скорее на сайт, чтобы посмотреть его',
        #     'leshev.da@mail.ru',
        #     ['leshev_aa@mail.ru'],
        #     fail_silently=False,
        # )