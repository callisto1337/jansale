from django.shortcuts import render
from .models import Product


def main(request):
    popular = Product.objects.all().filter(popular=True)[:4]
    new = Product.objects.all().filter(new=True)[:4]
    return render(request, 'app/index.html', {'popular': popular, 'new': new})
