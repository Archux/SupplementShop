from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *
from django.http import JsonResponse
import json
from django.views import generic
from django.contrib.auth.models import User


class HomeView(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = "products"


class SearchProductsView(ListView):
    model = Product
    template_name = 'shop/search_products.html'
    context_object_name = "products"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
        return object_list


class ProductDetails(DetailView):
    model = Product
    template_name = 'shop/product_details.html'
    context_object_name = "product"


class SpecialDealsView(ListView):
    model = Product
    template_name = 'shop/special_deals.html'
    context_object_name = "products"


class ProteinPowdersView(ListView):
    model = Product
    template_name = 'shop/protein_powders.html'
    context_object_name = "products"


class PreWorkoutView(ListView):
    model = Product
    template_name = 'shop/pre_workout.html'
    context_object_name = "products"


class CreatineView(ListView):
    model = Product
    template_name = 'shop/creatine.html'
    context_object_name = "products"


class MassGainersView(ListView):
    model = Product
    template_name = 'shop/mass_gainers.html'
    context_object_name = "products"


class BarsAndSnacksView(ListView):
    model = Product
    template_name = 'shop/bars_and_snacks.html'
    context_object_name = "products"


class VitaminsView(ListView):
    model = Product
    template_name = 'shop/vitamins.html'
    context_object_name = "products"


def cart(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = []
        items = []
        customer = []
    context = {"items": items, "order": order, "customer": customer}
    return render(request, 'shop/cart.html', context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', product_id)

    customer = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)

