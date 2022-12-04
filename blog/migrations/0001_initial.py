# Generated by Django 4.1.1 on 2022-12-04 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='Account-user.png', upload_to='blog_pics')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
