# Generated by Django 4.1.3 on 2022-11-18 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_alter_rent_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 18, 18, 50, 24, 817567, tzinfo=datetime.timezone.utc)),
        ),
    ]
