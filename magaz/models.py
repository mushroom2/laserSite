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
    user = models.OneToOneField(User, primary_key=True)
    site = models.CharField(blank=True, verbose_name='Сайт', max_length=150)
    skype = models.CharField(max_length=60, blank=True)
    profession = models.CharField(max_length=200, blank=True, verbose_name='професія')
    numb = models.CharField(blank=True, max_length=15, verbose_name='номер телефону')
    about = models.TextField(blank=True, verbose_name='про себе')
    avatar = models.ImageField(upload_to='userprofile/', blank=True, verbose_name='фото')

    def __str__(self):
        return self.user.username


class SiteUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    site = models.CharField(blank=True, verbose_name='Сайт', max_length=150)

    def __str__(self):
        return self.user.username


class SkypeUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    skype = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.user.username


class ProfessionalUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    profession = models.CharField(max_length=200, blank=True, verbose_name='професія')

    def __str__(self):
        return self.user.username


class NumbUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    numb = models.CharField(blank=True, max_length=15, verbose_name='номер телефону')

    def __str__(self):
        return self.user.username


class AboutUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    about = models.TextField(blank=True, verbose_name='про себе')

    def __str__(self):
        return self.user.username


class AvatarUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    avatar = models.ImageField(upload_to='userprofile/', blank=True, verbose_name='фото')

    def __str__(self):
        return self.user.username


class GoodPay(models.Model):
    user = models.ForeignKey(User, unique=False, verbose_name='користувач')
    prises = models.ForeignKey(Prises, null=True, blank=True, verbose_name='товар')
    date = models.DateTimeField(auto_now=True, primary_key=True, verbose_name='дата замовлення')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='ціна однієї одиниці')
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name='кількість')
    ordersum = models.PositiveIntegerField(null=True, blank=True, verbose_name='cума')

    def __str__(self):
        return self.user.username

