# Generated by Django 4.2.7 on 2023-11-21 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='food_photos')),
                ('description', models.TextField()),
                ('composition', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('type_of_food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodtype')),
            ],
        ),
    ]
