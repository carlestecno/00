# Generated by Django 3.1.7 on 2021-03-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temes', '0006_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
