# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0005_auto_20160504_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
                ('cat_pic', models.ImageField(upload_to='cat/')),
            ],
        ),
        migrations.AddField(
            model_name='prises',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magaz.Category'),
        ),
    ]
