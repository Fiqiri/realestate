# Generated by Django 3.2.12 on 2022-07-17 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Tiranë', 'Tiranë'), ('Kamëz', 'Kamëz'), ('Kavajë', 'Kavajë'), ('Rrogozhinë', 'Rrogozhinë'), ('Vorë', 'Vorë'), ('Durrës', 'Durrës'), ('Krujë', 'Krujë'), ('Shijak', 'Shijak'), ('Berat', 'Berat'), ('Kuçovë', 'Kuçovë'), ('Poliçan', 'Poliçan'), ('Skrapar', 'Skrapar'), ('Ura Vajgurore', 'Ura Vajgurore'), ('Bulqizë', 'Bulqizë'), ('Dibër', 'Dibër'), ('Klos', 'Klos'), ('Mat', 'Mat'), ('Belsh', 'Belsh'), ('Cërrik', 'Cërrik'), ('Elbasan', 'Elbasan'), ('Gramsh', 'Gramsh'), ('Librazhd', 'Librazhd'), ('Peqin', 'Peqin'), ('Prrenjas', 'Prrenjas'), ('Fier', 'Fier'), ('Lushnjë,', 'Lushnjë,'), ('Mallakastër', 'Mallakastër'), ('Patos', 'Patos'), ('Roskovec', 'Roskovec'), ('Divjakë', 'Divjakë'), ('Dropull', 'Dropull'), ('Gjirokastër', 'Gjirokastër'), ('Këlcyrë', 'Këlcyrë'), ('Libohovë', 'Libohovë'), ('Memaliaj', 'Memaliaj'), ('Përmet', 'Përmet'), ('Tepelenë', 'Tepelenë')], default='Tiranë', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.IntegerField(blank=True),
        ),
    ]
