# Generated by Django 4.1.1 on 2023-01-08 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0007_alter_lga_constituency_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='constituency_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='utilities.constituency'),
        ),
    ]
