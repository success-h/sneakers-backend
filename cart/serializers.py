from store.models import Product
from store.serializers import ProductSerializer
from .models import Cart
from rest_framework import serializers



class CartSerializer(serializers.ModelSerializer):
    products =  serializers.SerializerMethodField(
        'get_products',
        read_only=True
    )

    totalprice = serializers.SerializerMethodField(
        'get_total_price',
        read_only=True
    ) 
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity', 'products', 'id', 'totalprice']
        read_only_fields = ('id',),

    def get_products(self, obj):
        print("obj", obj.product.id)
        pd = Product.objects.filter(id=obj.product.id)
        return ProductSerializer(pd, many=True).data

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
