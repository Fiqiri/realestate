from django.db import models
from datetime import datetime
from relators.models import Relator

state_choices = [
    ('Berat', 'Berat'),
    ('Dibër', 'Dibër'),
    ('Durrës', 'Durrës'),
    ('Elbasan', 'Elbasan'),
    ('Fier', 'Fier'),
    ('Girokastër', 'Girokastër'),
    ('Korçë', 'Korçë'),
    ('Kukës', 'Kukës'),
    ('Lezhë', 'Lezhë'),
    ('Shkodër', 'Shkodër'),
    ('Tiranë', 'Tiranë'),
    ('Vlorë', 'Vlorë'),
]

type = [
    ('Shitje', 'Shitje'),
    ('Qera', 'Qera'),
]

class Listing(models.Model):
    relator = models.ForeignKey(Relator, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    shitje_qera = models.CharField(max_length=25, choices=type, default='Shitje')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, choices=state_choices, default='Tiranë')
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    area = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
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
