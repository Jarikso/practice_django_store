# Generated by Django 4.1.2 on 2023-01-25 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='ссылка')),
                ('chosen', models.BooleanField(default=False, verbose_name='избранная категория')),
                ('category_icon', models.ImageField(blank=True, upload_to='icon_category/', verbose_name='иконка')),
                ('category_img', models.ImageField(blank=True, upload_to='img_category/', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='название')),
                ('slug', models.SlugField(max_length=200, verbose_name='ссылка')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('available', models.BooleanField(default=True, verbose_name='наличие')),
                ('hot_offer', models.BooleanField(default=False, verbose_name='горячее предложение')),
                ('limited_edition', models.BooleanField(default=False, verbose_name='ограниченный тираж')),
                ('reviews', models.PositiveIntegerField(default=0, verbose_name='количество отзывов')),
                ('bought', models.PositiveIntegerField(default=0, verbose_name='куплено')),
                ('date_create', models.DateTimeField(verbose_name='дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='app_catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('id',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='полное имя')),
                ('description', models.TextField(max_length=200, verbose_name='отзыв')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='электронная почта')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='review', to='app_catalog.product', verbose_name='товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=20, verbose_name='Характеристика')),
                ('description', models.TextField(max_length=30, verbose_name='Описание')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='properties', to='app_catalog.product', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='img_product/', verbose_name='изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='image', to='app_catalog.product', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
