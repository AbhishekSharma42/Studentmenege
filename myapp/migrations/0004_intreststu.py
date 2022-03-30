# Generated by Django 3.2.9 on 2022-03-30 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_student_bran'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntrestStu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuName', models.CharField(max_length=20)),
                ('stuMob', models.CharField(max_length=10)),
                ('stuEmail', models.EmailField(max_length=254)),
                ('bran', models.CharField(default='', max_length=5)),
            ],
        ),
    ]