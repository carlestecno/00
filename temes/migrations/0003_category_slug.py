# Generated by Django 3.1.7 on 2021-03-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temes', '0002_auto_20210320_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]