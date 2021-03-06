# Generated by Django 3.2.7 on 2022-01-06 13:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_clientdataqrexe2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdataqrexe2',
            name='todaydate',
            field=models.DateField(default=datetime.date(2022, 1, 6)),
        ),
        migrations.CreateModel(
            name='clientdocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfdata', models.FileField(blank=True, null=True, upload_to='documents')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clientdataqrexe2')),
            ],
        ),
    ]
