from django.db import models
from products.models import Product
from courses.models import Course

class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('product', 'Product'),
        ('course', 'Course'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.order_type}"
