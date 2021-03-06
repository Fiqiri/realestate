# Generated by Django 3.2.12 on 2022-05-13 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20220404_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='unique_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='listing',
            name='zona',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Berat', 'Berat'), ('Dibër', 'Dibër'), ('Durrës', 'Durrës'), ('Elbasan', 'Elbasan'), ('Fier', 'Fier'), ('Girokastër', 'Girokastër'), ('Korçë', 'Korçë'), ('Kukës', 'Kukës'), ('Lezhë', 'Lezhë'), ('Shkodër', 'Shkodër'), ('Tiranë', 'Tiranë'), ('Vlorë', 'Vlorë')], default='Tiranë', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='shitje_qera',
            field=models.CharField(choices=[('Shitje', 'Shitje'), ('Qera', 'Qera'), ('Shitje/Qera', 'Shitje/Qera')], default='Shitje', max_length=25),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('Shqipëri', 'Shqipëri')], default='Tiranë', max_length=50),
        ),
    ]
