# Generated by Django 3.1.7 on 2021-03-21 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temes', '0003_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
