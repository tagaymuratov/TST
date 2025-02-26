# Generated by Django 5.1.1 on 2024-10-13 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Бренд')),
                ('img', models.ImageField(upload_to='imgs/brands', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Бренды',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Индустрия')),
            ],
            options={
                'verbose_name': 'Индустрии',
                'verbose_name_plural': 'Индустрии',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.SlugField(max_length=32, unique=True, verbose_name='Артикль')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tstapp.brands', verbose_name='Бренд')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tstapp.categories', verbose_name='Категорея')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tstapp.industries', verbose_name='Индустрия')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='imgs/products/', verbose_name='Изображение')),
                ('thumb', models.ImageField(blank=True, editable=False, upload_to='imgs/products/', verbose_name='Миниатюра')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tstapp.product', verbose_name='Артикль')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
