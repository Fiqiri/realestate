from django.db import models
from datetime import datetime
from relators.models import Relator

city_choices = [
    ('Tiranë', 'Tiranë'),
    ('Kamëz', 'Kamëz'),
    ('Kavajë', 'Kavajë'),
    ('Rrogozhinë', 'Rrogozhinë'),
    ('Vorë', 'Vorë'),
    ('Durrës', 'Durrës'),
    ('Krujë', 'Krujë'),
    ('Shijak', 'Shijak'),
    ('Berat', 'Berat'),
    ('Kuçovë', 'Kuçovë'),
    ('Poliçan', 'Poliçan'),
    ('Skrapar', 'Skrapar'),
    ('Ura Vajgurore', 'Ura Vajgurore'),
    ('Bulqizë', 'Bulqizë'),
    ('Dibër', 'Dibër'),
    ('Klos', 'Klos'),
    ('Mat', 'Mat'),
    ('Belsh', 'Belsh'),
    ('Cërrik', 'Cërrik'),
    ('Elbasan', 'Elbasan'),
    ('Gramsh', 'Gramsh'),
    ('Librazhd', 'Librazhd'),
    ('Peqin', 'Peqin'),
    ('Prrenjas', 'Prrenjas'),
    ('Fier', 'Fier'),
    ('Lushnjë,', 'Lushnjë,'),
    ('Mallakastër', 'Mallakastër'),
    ('Patos', 'Patos'),
    ('Roskovec', 'Roskovec'),
    ('Divjakë', 'Divjakë'),
    ('Dropull', 'Dropull'),
    ('Gjirokastër', 'Gjirokastër'),
    ('Këlcyrë', 'Këlcyrë'),
    ('Libohovë', 'Libohovë'),
    ('Memaliaj', 'Memaliaj'),
    ('Përmet', 'Përmet'),
    ('Tepelenë', 'Tepelenë'),
    ('Devoll', 'Devoll'),
    ('Kolonjë', 'Kolonjë'),
    ('Korçë', 'Korçë'),
    ('Maliq', 'Maliq'),
    ('Pustec', 'Pustec'),
    ('Pogradec', 'Pogradec'),
    ('Has', 'Has'),
    ('Kukës', 'Kukës'),
    ('Tropojë', 'Tropojë'),
    ('Kurbin', 'Kurbin'),
    ('Lezhë', 'Lezhë'),
    ('Mirditë', 'Mirditë'),
    ('Fushë-Arrëz', 'Fushë-Arrëz'),
    ('Malësi e Madhe', 'Malësi e Madhe'),
    ('Pukë', 'Pukë'),
    ('Shkodër', 'Shkodër'),
    ('Vau i Dejës', 'Vau i Dejës'),
    ('Vlorë', 'Vlorë'),
    ('Selenicë', 'Selenicë'),
    ('Sarandë', 'Sarandë'),
    ('Konispol', 'Konispol'),
    ('Himarë', 'Himarë'),
    ('Delvinë', 'Delvinë'),
    ('Finiq', 'Finiq'),

]

state_choices = [
    ('Shqipëri', 'Shqipëri'),
]

shitje_qera_choices = [
    ('Shitje', 'Shitje'),
    ('Qera', 'Qera'),
    ('Shitje/Qera', 'Shitje/Qera')
]

class Listing(models.Model):
    relator = models.ForeignKey(Relator, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    title_in_english = models.CharField(max_length=200, blank=True)

    shitje_qera = models.CharField(max_length=25, choices=shitje_qera_choices, default='Shitje')
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50, choices=state_choices, default='Tiranë')
    city = models.CharField(max_length=100, choices=city_choices, default='Tiranë')
    zona = models.CharField(max_length=100)
    location_link = models.TextField(blank=True, default="https://www.google.com/maps/place/41%C2%B012'40.3%22N+19%C2%B031'10.6%22E/@41.2111862,19.5174121,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x605debbc8ae35cf4!8m2!3d41.2111862!4d19.5196008?hl=en")
    unique_code = models.CharField(max_length=10, unique=True)

    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    description_in_english = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    area = models.IntegerField()
    lot_size = models.IntegerField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
