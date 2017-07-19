# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='prof_pics/')),
                ('description', models.TextField(blank=True, max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
