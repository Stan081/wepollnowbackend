# Generated by Django 4.1.1 on 2022-11-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]