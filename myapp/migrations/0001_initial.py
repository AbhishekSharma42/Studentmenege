# Generated by Django 3.2.9 on 2022-03-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuName', models.CharField(max_length=20)),
                ('stuMob', models.CharField(max_length=10)),
                ('stu', models.EmailField(max_length=254)),
            ],
        ),
    ]
