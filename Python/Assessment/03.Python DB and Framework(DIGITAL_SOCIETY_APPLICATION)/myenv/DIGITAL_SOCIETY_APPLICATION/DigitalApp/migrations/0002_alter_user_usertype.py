# Generated by Django 5.1.3 on 2024-11-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('member', 'Member'), ('watchman', 'Watchman')], max_length=10),
        ),
    ]
