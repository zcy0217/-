# Generated by Django 3.2.18 on 2023-10-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_auto_20231014_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='choice4',
            field=models.CharField(default='室內', max_length=50),
        ),
    ]
