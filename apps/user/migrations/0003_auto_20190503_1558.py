# Generated by Django 2.1.7 on 2019-05-03 15:58

import apps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar_default.png', upload_to=apps.user.models.user_directory_path, verbose_name='头像'),
        ),
    ]
