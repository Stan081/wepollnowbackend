# Generated by Django 4.1.1 on 2022-12-04 01:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(default='Presidential Election', max_length=40)),
                ('poll_date', models.DateTimeField(auto_now_add=True)),
                ('poll_startDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('poll_endDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PollCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
