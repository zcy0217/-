# Generated by Django 3.2.18 on 2023-10-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_preference_choice4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference_food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice5', models.CharField(max_length=50)),
                ('choice6', models.CharField(max_length=50)),
            ],
        ),
    ]
