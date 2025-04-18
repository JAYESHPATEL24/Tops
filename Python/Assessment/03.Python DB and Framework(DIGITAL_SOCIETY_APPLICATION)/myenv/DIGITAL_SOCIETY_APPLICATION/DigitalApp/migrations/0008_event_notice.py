# Generated by Django 5.1.3 on 2024-11-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalApp', '0007_alter_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=20)),
                ('eventdescription', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('createeventtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticename', models.CharField(max_length=20)),
                ('noticedescription', models.TextField()),
                ('createnoticetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
