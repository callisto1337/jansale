# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171129_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(blank=True, default='asd', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
    ]
