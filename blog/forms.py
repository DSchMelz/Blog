from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):#вмесо form.Form пишем такой, он позволяет писать меньше кода
    #вместо ручноп=го update'а пишем его через класс+ словарь

    # title = forms.CharField(max_length = 50)#в формах charfield = input
    # slug = forms.CharField(max_length = 50)
    # title.widget.attrs.update({"class": "form-control"})
    # #чтобы задать класс или другой атрибут в бок, который джанго создаёт
    # #автоматом, например в формах инпут, нужно прописать верхнюю строку
    # #и передать в de update ключом class, а значением бутстраповский класс(form-control)
    # slug.widget.attrs.update({"class": "form-control"})
    class Meta:
        model = Tag
        fields = ["title", "slug"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()
        if new_slug == "create":
            raise ValidationError("Slug may not be Create")
        if Tag.objects.filter(slug__iexact=new_slug).count():#если есть ещё slug = данному, count найдёт значение не = 0
            raise ValidationError("Slug must be unique. '{0}' slug've already exist".format(new_slug.capitalize()))#capitalize - метод для увеличения первой буквы строки

        return new_slug

    #если наш класс по создани. тэга будет наследоваться от ModelForm, а не от Form, то save() нам не нужен, (он сохраняется автоматом)
    #надпись сверху не гарантирует правильность
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ["title", "slug", "body", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class":"form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"})
        }
    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()
        if new_slug == "create":
            raise ValidationError("Slug may not be Create")
        return new_slug
    # def save(self):
    #     new_tag = Tag.objects.create(title = self.cleaned_data['title'], slug = self.cleaned_data['slug'])
    #     #cleaned_data - словарь с сохранёнными данными в форме. Он появляется, если данные есть и они корректны
    #     return new_tag