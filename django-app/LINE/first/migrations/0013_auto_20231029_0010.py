# Generated by Django 3.2.18 on 2023-10-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0012_auto_20231029_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.RemoveField(
            model_name='preference_food',
            name='user',
        ),
    ]
