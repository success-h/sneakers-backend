import re
from rest_framework import serializers
from store.models import Product, Category, ProductImage, Category



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name', 'slug', 'id']
        read_only_fields = ['id']


    
    
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', 'name',]
        read_only_fields = ('id',)





class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'description', 'price', 'image']
        read_only_fields = ['id']


    def get_images(self, obj):
        print("[img]", obj)
        img = obj.image_set.all()
        serializer = ProductImageSerializer(img, many=True)
        return serializer.data

    

