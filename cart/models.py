from django.db import models
from store.models import Product
from users.models import User

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'

    def get_total_price(self):
        return self.quantity * self.product.price

    def get_total_price_after_discount(self):
        return self.quantity * self.product.price_after_discount

    def get_total_discount(self):
        return self.quantity * self.product.discount

    def get_total_price_after_discount_and_tax(self):
        return self.quantity * self.product.price_after_discount_and_tax

