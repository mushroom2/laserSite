from django.db import models


class Category (models.Model):
    cat_name = models.CharField(max_length=30)
    cat_pic = models.ImageField(upload_to='cat/')
    slag_url = models.SlugField(max_length=42,
                                help_text='якщо все вийде- то це буде ссиль')

    def __str__(self):
        return self.cat_name


class Prises (models.Model):
    good_name = models.CharField(max_length=200)
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