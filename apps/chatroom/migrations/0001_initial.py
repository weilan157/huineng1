# Generated by Django 2.1.7 on 2019-06-02 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(default='未命名分组', max_length=10, verbose_name='分组名')),
            ],
            options={
                'verbose_name': '聊天分组',
                'verbose_name_plural': '聊天分组',
            },
        ),
        migrations.CreateModel(
            name='ChatLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('chat_describe', models.CharField(max_length=255, verbose_name='聊天内容')),
                ('chat_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_user', to=settings.AUTH_USER_MODEL, verbose_name='发送用户')),
                ('to_chat_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_chat_user', to=settings.AUTH_USER_MODEL, verbose_name='接收用户')),
            ],
            options={
                'verbose_name': '聊天记录',
                'verbose_name_plural': '聊天记录',
            },
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='chat_log',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_log', to='chatroom.ChatLog', verbose_name='组内成员'),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='chat_owned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_owned', to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
    ]