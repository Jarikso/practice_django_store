# Generated by Django 4.1.2 on 2023-01-25 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_order', models.CharField(max_length=5, unique=True, verbose_name='номер заказа')),
                ('full_name', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='полное имя')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='электронная почта')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='телефон')),
                ('delivery', models.CharField(blank=True, max_length=2, verbose_name='доставка')),
                ('city', models.CharField(blank=True, max_length=25, verbose_name='город')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='адрес')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('pay_method', models.CharField(blank=True, max_length=2, verbose_name='способ оплаты')),
                ('paid', models.BooleanField(default=False, verbose_name='статус оплаты')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app_orders.order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='app_catalog.product', verbose_name='')),
            ],
        ),
    ]
