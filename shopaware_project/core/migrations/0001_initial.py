# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(max_length=1000)),
                ('website', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]