import re
from django.db import models
from users.models import User
from django.urls import reverse
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    id=models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)

    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])
    
    def generate_slug(self):
        if self.name:
            self.slug = re.sub('[^\w\s-]', '', self.name).replace(' ', '-').lower()
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.generate_slug()
        super().save(*args, **kwargs)



class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, blank=False, null=True)
    image = models.ImageField(upload_to='products/images/')
    name = models.CharField(max_length=255, default='')
    id=models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    

    def __str__(self):
        return self.product.name




class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.name

    def generate_slug(self):
        if self.name:
            self.slug = re.sub('[^\w\s-]', '', self.name).replace(' ', '-').lower()
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.generate_slug()
        super().save(*args, **kwargs)