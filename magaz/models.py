from django.contrib.auth.models import User
from django.db import models


class Category (models.Model):
    cat_name = models.CharField(max_length=30)
    cat_pic = models.ImageField(upload_to='cat/')
    slag_url = models.SlugField(max_length=42,
                                help_text='якщо все вийде- то це буде ссиль')

    def __str__(self):
        return self.cat_name


class Prises (models.Model):
    good_name = models.CharField(max_length=200, db_index=True)
    good_price = models.IntegerField('price')
    good_about = models.TextField()
    pic = models.ImageField(upload_to='shop/')
    good_time = models.DateTimeField('date_published')
    in_magaz = models.BooleanField(default=True, help_text='наличие товара на складе', db_index=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)


    def get_in_magaz(self):
        if self.in_magaz:
            return '+'
        else:
            return ''

    def __str__(self):
        return self.good_name

    def shortMagazText(self):
        if len(self.good_about) > 105:
            return self.good_about[:105] + '...'
        else:
            return self.good_about


class MyUser(models.Model):
    user = models.OneToOneField(User)

    site = models.URLField(blank=True)
    skype = models.CharField(max_length=60, blank=True)
    profession = models.CharField(max_length=200, blank=True)
    numb = models.IntegerField('numb', blank=True, default=None)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='userprofile/', blank=True)

    def __str__(self):
        return self.user.username