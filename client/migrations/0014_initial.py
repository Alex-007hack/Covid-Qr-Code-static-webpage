# Generated by Django 4.0 on 2022-01-22 18:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0013_remove_clientdataqrexe2_client_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('pwd', models.CharField(max_length=30)),
                ('contactno', models.CharField(max_length=15)),
                ('adhar', models.CharField(default='000000000000', max_length=12)),
                ('photo', models.ImageField(upload_to='client_data')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='clientdataqrexe2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.TextField(default=None, null=True)),
                ('hadcovid19', models.CharField(max_length=5)),
                ('coviddate', models.DateField(blank=True, default=None, null=True)),
                ('vaccinated', models.CharField(max_length=5)),
                ('first_dose', models.DateField(blank=True, null=True)),
                ('second_dose', models.DateField(blank=True, null=True)),
                ('contact_covid', models.CharField(max_length=5)),
                ('cotact_date', models.DateField(blank=True, null=True)),
                ('passanger', models.CharField(max_length=5)),
                ('covid_test', models.CharField(max_length=5)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('reference', models.CharField(default='', max_length=30)),
                ('todaydate', models.DateField(default=datetime.date(2022, 1, 22))),
                ('status', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='clientdocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfdata', models.FileField(blank=True, null=True, upload_to='documents')),
                ('qrdata', models.ImageField(blank=True, null=True, upload_to='qrcode')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clientdataqrexe2')),
            ],
        ),
    ]