# Generated by Django 4.1.7 on 2024-04-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='movie/images/default.jpg', upload_to='movie/images/'),
        ),
    ]