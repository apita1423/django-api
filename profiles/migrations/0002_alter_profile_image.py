# Generated by Django 3.2.25 on 2024-04-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../https://res.cloudinary.com/db5hwihda/image/upload/v1713298366/default_profile_yvc7xn.jpg', upload_to='images/'),
        ),
    ]
