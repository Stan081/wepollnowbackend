# Generated by Django 4.1.1 on 2022-11-08 09:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilities', '0001_initial'),
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('device_id', models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('valid_voters_card', models.BooleanField(default='False')),
                ('residential_status', models.BooleanField(default='True')),
                ('age_range', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('marital_status', models.IntegerField()),
                ('religion', models.IntegerField()),
                ('employment_status', models.IntegerField()),
                ('accomodation_status', models.IntegerField()),
                ('first_time_voter', models.BooleanField(default='False')),
                ('diaspora_voter', models.BooleanField(default='False')),
                ('resident_lga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lgaOfResidence', to='utilities.lga')),
                ('resident_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stateOfResidence', to='utilities.state')),
                ('state_of_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stateOfOrigin', to='utilities.state')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted_at', models.DateTimeField()),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='utilities.candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.poll')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voters.voter')),
            ],
        ),
    ]
