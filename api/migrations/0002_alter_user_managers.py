# Generated by Django 4.0.5 on 2022-07-01 09:15

from django.db import migrations

import api.models.user


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', api.models.user.UserManager()),
            ],
        ),
    ]