# Generated by Django 4.2.7 on 2023-12-25 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзинка',
                'verbose_name_plural': 'Корзинки',
            },
        ),
        migrations.CreateModel(
            name='BasketFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('amount', models.PositiveSmallIntegerField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basketmodel', verbose_name='Корзинка')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food', verbose_name='Еда')),
            ],
            options={
                'verbose_name': 'Еда в корзинке',
                'verbose_name_plural': 'Еда в корзинке',
            },
        ),
    ]
