# Generated by Django 4.2 on 2023-05-08 18:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pins", "0002_alter_pin_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="pin",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="pin",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="pin",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
