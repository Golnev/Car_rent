# Generated by Django 4.1.3 on 2022-11-18 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 18, 16, 6, 33, 122371, tzinfo=datetime.timezone.utc)),
        ),
    ]