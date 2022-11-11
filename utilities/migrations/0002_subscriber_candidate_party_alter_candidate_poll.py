# Generated by Django 4.1.1 on 2022-11-11 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
        ('utilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utilities.party'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.poll'),
        ),
    ]