# Generated by Django 4.0.3 on 2022-04-12 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('photo', models.ImageField(default='пусто', upload_to='photos/%y%m/%d')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['date', 'title'],
            },
        ),
    ]
