from django.shortcuts import render
from .models import *

def main (request):
    products = Product.objects.all()
    return render (request, 'main.html', {'products':products})

def cart (request):
    return render (request, 'cart.html')

def detail (request):
    return render (request, 'product_detail.html')