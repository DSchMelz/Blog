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

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)# берём тэг по слагу из бд
        bound_form = self.model_form(instance = obj)
        return render(request, self.template, context={"form": bound_form, self.model.__name__.lower(): obj})
    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)# берём тэг по слагу из бд
        bound_form = self.model_form(request.POST, instance = obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={"form": bound_form, self.model.__name__.lower(): obj})

class ObjectDeleteMixin:
    model = None
    template = None
    redirectUrl = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirectUrl))