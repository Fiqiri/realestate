# Generated by Django 3.2.12 on 2022-03-14 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relator',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]