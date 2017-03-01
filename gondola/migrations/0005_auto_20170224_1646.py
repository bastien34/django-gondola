# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gondola.models


class Migration(migrations.Migration):

    dependencies = [
        ('gondola', '0004_auto_20170224_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gondola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', validators=[gondola.models.validate_gondola])),
                ('link_to', models.URLField(blank=True, null=True)),
                ('label', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gondolerow',
            name='image_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_image', to='gondola.Gondola'),
        ),
        migrations.AlterField(
            model_name='gondolerow',
            name='image_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_image', to='gondola.Gondola'),
        ),
        migrations.AlterField(
            model_name='gondolerow',
            name='image_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_image', to='gondola.Gondola'),
        ),
    ]