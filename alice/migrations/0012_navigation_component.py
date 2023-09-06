# Generated by Django 4.2.4 on 2023-09-03 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alice', '0011_rename_url_navigation_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='component',
            field=models.CharField(default=django.utils.timezone.now, max_length=64, unique=True),
            preserve_default=False,
        ),
    ]