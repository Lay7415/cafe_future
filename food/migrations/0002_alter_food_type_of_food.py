# Generated by Django 4.2.7 on 2023-11-21 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_of_food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodtype', verbose_name='Тип еды'),
        ),
    ]
