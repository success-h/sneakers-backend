from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Category, Product, ProductImage
from .serializers import  ProductSerializer, CategorySerializer , ProductImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains') 
    class Meta:
        model = Product
        fields = ('name',)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    permisson_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

        
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)