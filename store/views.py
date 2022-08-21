from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from cart.serializers import CartSerializer

from cart.models import Cart
from .models import Category, Product, ProductImage
from .serializers import  ProductSerializer, CategorySerializer , ProductImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains') 
    class Meta:
        model = Product
        fields = ('name', 'slug')


class CategoryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains') 
    class Meta:
        model = Category
        fields = ('name',)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filterset_class = CategoryFilter

        
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)




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