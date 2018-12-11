from django.db import models
from django.urls import reverse


class Art(models.Model):
    title = models.CharField(max_length=120)
    original_title = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='art_images')
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("gallery:art-detail", kwargs={'id': self.id})

    def __str__(self):
        return self.title
