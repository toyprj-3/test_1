# Generated by Django 4.2.2 on 2023-06-27 10:13

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
