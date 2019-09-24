# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-24 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
