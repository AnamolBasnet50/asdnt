
from django.db import models
import cloudinary.models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = cloudinary.models.CloudinaryField('image')  # Store product images in Cloudinary

    def __str__(self):
        return self.name
