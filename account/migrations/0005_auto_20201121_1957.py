# Generated by Django 3.1.3 on 2020-11-21 18:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201121_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 18, 57, 36, 520069, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 18, 57, 36, 520069, tzinfo=utc)),
        ),
    ]