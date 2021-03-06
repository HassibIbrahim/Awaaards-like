# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-03 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(blank=True, default=0)),
                ('usability', models.IntegerField(blank=True, default=0)),
                ('creativity', models.IntegerField(blank=True, default=0)),
                ('content', models.IntegerField(blank=True, default=0)),
                ('overall_score', models.IntegerField(blank=True, default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.Project')),
            ],
        ),
    ]
