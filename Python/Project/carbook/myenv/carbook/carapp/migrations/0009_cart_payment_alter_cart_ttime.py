# Generated by Django 5.1.3 on 2024-12-11 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0008_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='ttime',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 11, 5, 56, 5, 996644, tzinfo=datetime.timezone.utc)),
        ),
    ]
