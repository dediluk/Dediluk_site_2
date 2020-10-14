# Generated by Django 3.1.1 on 2020-09-07 18:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='author/', verbose_name='Изображение')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='book/', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books_author', to='mybooks.Author', verbose_name='Авторы'),
        ),
    ]
