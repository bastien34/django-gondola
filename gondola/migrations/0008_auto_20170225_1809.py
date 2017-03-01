# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gondola', '0007_auto_20170225_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='gondolerow',
            name='images',
            field=models.ManyToManyField(to='gondola.Gondola'),
        ),
        migrations.AlterField(
            model_name='gondola',
            name='link_to',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]