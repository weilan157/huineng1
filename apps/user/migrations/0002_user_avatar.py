# Generated by Django 2.1.7 on 2019-04-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', upload_to='avatar/', verbose_name='头像'),
        ),
    ]