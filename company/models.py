from django.db import models


class SocialMedia(models.Model):
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    pinterest = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.email


