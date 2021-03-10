# Generated by Django 3.1.7 on 2021-03-09 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_follow_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Группа, в которой опубликуется ваш пост.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='api.group', verbose_name='Группа!'),
        ),
    ]
