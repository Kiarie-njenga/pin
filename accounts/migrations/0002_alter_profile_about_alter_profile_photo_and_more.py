# Generated by Django 4.1.1 on 2023-03-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="about",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=models.ImageField(default="default.png", upload_to="profiles"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="pronouns",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="profile",
            name="website",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]