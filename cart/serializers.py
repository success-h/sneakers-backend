from store.models import ProductImage
from .models import Cart
from rest_framework.serializers import ModelSerializer



class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
    depth = 1