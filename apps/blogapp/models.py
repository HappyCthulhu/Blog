from django.db import models
from datetime import datetime
from pytils.translit import slugify
from django.shortcuts import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    body = models.TextField(max_length=5000, verbose_name="Основной текст")
    date = models.DateTimeField(default=datetime.now, null=True, verbose_name="Дата создания")
    image = models.ImageField(blank=True, default='media/Map-Navigation.jpg', upload_to='media', verbose_name="картинка")
    #author =
    slug = models.SlugField(unique=True, verbose_name="url")


    def get_absolute_url(self):
        return reverse('post', kwargs={'slug':self.slug})


    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-date']

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    message = models.TextField(max_length=500, verbose_name="пиьсмо")
    phone = models.CharField(max_length=15, verbose_name="телефон")
    email = models.EmailField(verbose_name="емайл")
