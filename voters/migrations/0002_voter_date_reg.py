# Generated by Django 4.1.1 on 2023-01-09 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='date_reg',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
