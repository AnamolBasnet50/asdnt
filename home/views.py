from django.shortcuts import render
from products.models import Product  # Assuming you have a Product model

def home(request):
    products = Product.objects.all()[:3]  # Show 3 featured products
    return render(request, "index.html", {"products": products})
