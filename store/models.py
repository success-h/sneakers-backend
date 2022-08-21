import re
from django.db import models
from users.models import User
from django.urls import reverse
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')
    name = models.CharField(max_length=255, db_index=True, default='')

    def __str__(self):
        return self.product.name




class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

    # def slugify(self, value):
    #     result = re.sub('[^\w\s-]', '', value)
    #     result = re.sub('[-\s]+', '-', result)
    #     return result.lower()

    # def generate_slug(self):
    #     self.slug = self.slugify(self.name)
    #     return self.slug