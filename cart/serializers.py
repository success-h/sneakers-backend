from store.models import Product
from store.serializers import ProductSerializer
from .models import Cart
from rest_framework import serializers



class CartSerializer(serializers.ModelSerializer):
    products =  serializers.SerializerMethodField(
        'get_products',
        read_only=True
    )
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity', 'products', 'id']
        read_only_fields = ('id',),

    def get_products(self, obj):
        pd = Product.objects.filter(id=obj.product.id)
        return ProductSerializer(pd, many=True).data


