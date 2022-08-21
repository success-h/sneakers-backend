from django.shortcuts import render
from rest_framework import viewsets

from cart.models import Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters


# Create your views here.
class CartFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains') 
    class Meta:
        model = Cart
        fields = ('user', 'product',)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    ordering_fields = ('user',)
    ordering = ('user',)
    permisson_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = CartFilter

