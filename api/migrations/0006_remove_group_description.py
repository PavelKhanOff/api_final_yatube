# Generated by Django 3.1.7 on 2021-03-10 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210310_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
    ]
