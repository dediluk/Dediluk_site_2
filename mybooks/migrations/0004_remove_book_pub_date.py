# Generated by Django 3.1.1 on 2020-09-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0003_auto_20200907_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
    ]
