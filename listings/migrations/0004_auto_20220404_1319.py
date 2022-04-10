# Generated by Django 3.2.12 on 2022-04-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='shitje_qera',
            field=models.CharField(choices=[('Shitje', 'Shitje'), ('Qera', 'Qera')], default='Shitje', max_length=25),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]