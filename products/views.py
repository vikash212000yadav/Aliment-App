from django.shortcuts import render

# Create your views here.
from products.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})