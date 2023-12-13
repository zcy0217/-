# Generated by Django 4.2.7 on 2023-12-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('staytime', models.CharField(max_length=20, null=True)),
                ('blogsrc', models.CharField(max_length=1024, null=True)),
                ('summary', models.CharField(max_length=1024, null=True)),
                ('city', models.CharField(max_length=5)),
                ('address', models.CharField(default='', max_length=256)),
                ('tel', models.CharField(max_length=20, null=True)),
                ('time', models.CharField(max_length=256, null=True)),
                ('remark', models.CharField(max_length=256, null=True)),
                ('restday', models.CharField(max_length=20, null=True)),
                ('website', models.CharField(max_length=1024, null=True)),
                ('socialwebsite', models.CharField(max_length=1024, null=True)),
                ('star', models.CharField(default='', max_length=3, null=True)),
                ('price', models.CharField(default=0, max_length=10)),
                ('nobarrier', models.CharField(max_length=1)),
                ('parking', models.CharField(max_length=1)),
                ('restaurantfood', models.CharField(max_length=4, null=True)),
                ('streetfood', models.CharField(max_length=4, null=True)),
                ('child', models.CharField(max_length=4, null=True)),
                ('group', models.CharField(max_length=4, null=True)),
                ('indoor', models.CharField(max_length=4, null=True)),
                ('outdoor', models.CharField(max_length=4, null=True)),
                ('travel_type', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
