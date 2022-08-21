from store.models import Product
from store.serializers import ProductSerializer
from .models import Cart
from rest_framework import serializers



class CartSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(
        read_only=True,
        method_name='get_products'
    )
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity']
        read_only_fields = ('id',)

    def get_products(self, obj):
        product = Product.objects.filter(cart=obj)
        serializers = ProductSerializer(product, many=True)
        return serializers.data

    