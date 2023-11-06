# Generated by Django 4.2.6 on 2023-11-04 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000000)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 5, 0, 54, 38, 435791))),
            ],
        ),
    ]
