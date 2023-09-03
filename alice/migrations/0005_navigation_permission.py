# Generated by Django 4.2.4 on 2023-08-31 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('alice', '0004_navigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='permission',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.permission'),
            preserve_default=False,
        ),
    ]
