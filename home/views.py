from django.shortcuts import render
from django.http import HttpResponseServerError
from products.models import Product  # Ensure this import is correct

def home(request):
    try:
        products = Product.objects.all()[:3]  # Fetch products safely
        return render(request, "index.html", {"products": products})
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {e}")
