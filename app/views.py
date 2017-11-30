from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def main(request):
    popular = Product.objects.all().filter(popular=True)[:4]
    new = Product.objects.all().filter(new=True)[:4]
    categories = Category.objects.all()

    return render(request, 'app/main.html', {
        'popular': popular, 'new': new,
        'categories': categories}
    )


def category(request, url):
    data_category = get_object_or_404(Category, url=url)
    category_items = Product.objects.all().filter(category=data_category.pk)
    categories = Category.objects.all()

    return render(request, 'app/category.html', {
        'data_category': data_category,
        'category_items': category_items,
        'categories': categories}
    )


def contacts(request):
    categories = Category.objects.all()

    return render(request, 'app/contacts.html', {
        'categories': categories}
    )
