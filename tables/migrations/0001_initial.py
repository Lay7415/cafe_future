# Generated by Django 4.2.7 on 2023-11-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='table_photos', verbose_name='Фотография')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('table_number', models.PositiveIntegerField(verbose_name='Номер Столика')),
                ('type', models.CharField(choices=[(1, 'Обычный'), (2, 'VIP'), (3, 'Кабинки')], max_length=20, verbose_name='Тип')),
            ],
        ),
    ]
