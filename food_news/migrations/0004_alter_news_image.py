# Generated by Django 4.2.7 on 2023-11-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_news', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
