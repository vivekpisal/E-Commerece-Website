from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class Type(models.Model):
	category=models.CharField(max_length=20)

	def __str__(self):
		return f'{self.category}'


class Product(models.Model):
	category=models.ForeignKey(Type,on_delete=models.CASCADE,related_name='product')
	name=models.CharField(max_length=20)
	price=models.IntegerField()
	description=models.TextField(default=None)
	pic=models.ImageField(upload_to='product/')


	def __str__(self):
		return f'{self.name}'



class Cart(models.Model):
	li=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart')
	name=models.CharField(max_length=20)
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)


	def __str__(self):
		return f'Name:{self.name} Item:{self.li}'


class Order(models.Model):
	li=models.ForeignKey(User,on_delete=models.CASCADE,related_name='order')
	address=models.TextField()
	pincode=models.IntegerField()
	mobno=models.IntegerField()
	ordertime=models.DateTimeField(default=timezone.now)
	cart=models.ManyToManyField(Cart,null=True,blank=True)
	product=models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE)


	def __str__(self):
		return f'Cart:{self.cart}  Product:{self.product} Pincode {self.pincode}' 
