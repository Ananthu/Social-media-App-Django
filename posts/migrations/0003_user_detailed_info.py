# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Detailed_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone_no', models.IntegerField(blank=True, default=0)),
                ('about', models.TextField(blank=True)),
                ('profile_pic', models.FileField(blank=True, upload_to=b'')),
            ],
        ),
    ]
