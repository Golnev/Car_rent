# Generated by Django 4.1.3 on 2022-11-07 14:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 14, 13, 43, 452564, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48, verbose_name='name')),
                ('message', models.TextField(verbose_name='message text')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 11, 7, 14, 13, 43, 453561, tzinfo=datetime.timezone.utc), verbose_name='date comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post comment')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'blog_comments',
                'ordering': ('date_created',),
            },
        ),
    ]