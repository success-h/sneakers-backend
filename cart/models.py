from django.db import models
from store.models import Product
from users.models import User
import uuid

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    id=models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)


    def __str__(self):
        return f'{self.product.name} - {self.quantity}'

    def total_price(self):
        return self.quantity * self.product.price

