# Generated by Django 4.0.1 on 2022-01-27 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default=datetime.datetime(2022, 1, 27, 13, 47, 9, 864082, tzinfo=utc))),
            ],
        ),
    ]
