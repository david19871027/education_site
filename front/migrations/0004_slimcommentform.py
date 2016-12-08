# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments_xtd', '0002_blacklisteddomain'),
        ('front', '0003_auto_20161129_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlimCommentForm',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.XtdComment')),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('submit_date',),
                'abstract': False,
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'permissions': [('can_moderate', 'Can moderate comments')],
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
    ]
