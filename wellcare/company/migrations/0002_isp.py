# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-21 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('review_date', models.DateField()),
                ('full_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('funding', models.CharField(choices=[(1, 'Not relevant'), (2, 'Review'), (3, 'Maybe relevant'), (4, 'Relevant'), (5, 'Leading candidate')], max_length=10)),
            ],
        ),
    ]
