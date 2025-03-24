from django.urls import path
from .views import checkout_product, checkout_course, checkout_success

urlpatterns = [
    path('checkout/product/<int:product_id>/', checkout_product, name='checkout_product'),
    path('checkout/course/<int:course_id>/', checkout_course, name='checkout_course'),
    path('checkout/success/', checkout_success, name='checkout_success'),
]
