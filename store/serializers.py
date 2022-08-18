import re
from rest_framework import serializers
from store.models import Product, Category, ProductImage, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image', 'name')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True, many=True)


    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'description', 'price', 'image']
        read_only_fields = ['id']
    

    def get_images(self, obj):
        images = obj.image_set.all()
        serializers = ProductImageSerializer(images, many=True)
        return serializers.data

    def slugify(self, value):
        result = re.sub('[^\w\s-]', '', value)
        result = re.sub('[-\s]+', '-', result)
        return result.lower()

    def create(self, validated_data):
        images = validated_data.pop('image')
        product = Product.objects.create(**validated_data)
        slug = self.slugify(product.name)
        product.slug = slug
        for image in images:
            ProductImage.objects.create(product=product, **image)
        return product

    

