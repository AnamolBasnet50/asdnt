from django.shortcuts import render, get_object_or_404, redirect
from .forms import CheckoutForm
from .models import Order
from products.models import Product
from courses.models import Course

def checkout_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_type = 'product'
            order.product = product
            order.save()
            return redirect('checkout_success')

    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html', {'form': form, 'item': product, 'type': 'product'})

def checkout_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_type = 'course'
            order.course = course
            order.save()
            return redirect('checkout_success')

    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html', {'form': form, 'item': course, 'type': 'course'})

def checkout_success(request):
    return render(request, 'orders/checkout_success.html')
