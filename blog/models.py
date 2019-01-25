from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
# Create your models here.

def gen_slug(s):#делаем генерациюслага
    new_slug = slugify(s, allow_unicode=True)#эта функция ставит всё в нижн регистр, убирает запреш знаки
    #alllow_unicode позвояет использовать символы юникода, например русские буквы
    return new_slug

class Post(models.Model):#создаём класс Post для работы с бд
    title = models.CharField(max_length = 150, db_index = True)#заголовок
    slug = models.SlugField(max_length = 150, blank = True, unique = True)#ссылка понятая для юзера(должна быть уникальной)
    body = models.TextField(blank = True, db_index = True)#тело текста
    date_pub = models.DateField(auto_now_add = True)#время публикации
    tags = models.ManyToManyField("Tag", blank = True, related_name = "posts")
    #связывем post с tag, разрешаем, чтобы  можно было тэг не ставить, и связываем с относящимся именем posts

    def __str__(self):#именем при вызове показа будет строка title'а
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:#если у слага нет id(не был указан слаг), то он генерит слаг с таким названием "название тайтла-время создания"
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse("post_update_url", kwargs={"slug": self.slug})

    def get_absolute_url(self):#имя функции - лучше использовать такое
        return reverse("post_detail_url", kwargs = {"slug": self.slug})
    def get_delete_url(self):
        return reverse("post_delete_url", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-date_pub"]#посты будут сортироваться для пагинатора так: самые новые вверху, старые внизу(-)указываем для этого
    #тоже самое, что прописывать ссылку со slug'ом в html полностью({% url 'post_detail_url' slug=post.slug %})
    #импортируем reverse, он генерирует нам ссылку

    #ччтобы загрущить что-то в бд имеется 2 способа
    #в обоих способах нужно зайти в консоль django
    #manage.py shell
    #затем нужно импортировать ваш класс
    #from blog.models import Post

    #1способ: post1 = Post(title = "...", slug = "...", body = "...")
    #и после этого нужно post1.save()
    #2способ: post1 = Post.objects.create(title = "...", slug = "...", body = "...")
    #но после этого не нужно сохранять

    #после этого можно получать разную инфу об элементах
    #1 - post1.id
    #можно получать зн методов переданных классу
    #например post1.title, post1.date_pub и т.д

class Tag(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, unique = True)
    def __str__(self):#именем при вызове показа будет строка title'а
        return self.title
    #чтобы связать что-то с чем-то, нам нужно в одном из этих элементов укзать
    #tags = models.ManyToManyField("Tag", blank = True, related_name = "posts")
    def get_absolute_url(self):#имя функции - лучше использовать такое
        return reverse("tag_detail_url", kwargs = {"slug": self.slug})
    def get_update_url(self):
        return reverse("tag_update_url", kwargs={"slug": self.slug})
    def get_delete_url(self):
        return reverse("tag_delete_url", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["title"]#в алф порядке