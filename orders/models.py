from django.db import models
from utils.generate_code import generate_code
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product


# Create your models here.


CART_STATUS = (
    ('inprogress','inprogress'),
    ('completed','completed'),
    
)


class Cart (models.Model):
    code = models.CharField(max_length=8,default=generate_code)
    user = models.ForeignKey(User,related_name='user_cart',on_delete=models.CASCADE)
    status = models.CharField(max_length=18,choices=CART_STATUS)

    def __str__(self):
        return self.code



    def get_total (self):
        total = 0
        for product in self.cart_detail.all():
            total += product.total
            return total
    



class CartDetail (models.Model):
    order = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,null=True,blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.order)












ORDER_STATUS = (
    ('received','received'),
    ('processed','processed'),
    ('shiped','shiped'),
    ('delivered','delivered'),
)


class Order (models.Model):
    code = models.CharField(max_length=8,default=generate_code)
    user = models.ForeignKey(User,related_name='user_order',on_delete=models.CASCADE)
    status = models.CharField(max_length=18,choices=ORDER_STATUS)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.code



class OrderDetail (models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order)
        

