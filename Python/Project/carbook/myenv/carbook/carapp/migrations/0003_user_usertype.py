# Generated by Django 5.1.3 on 2024-11-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='customer', max_length=20),
        ),
    ]
