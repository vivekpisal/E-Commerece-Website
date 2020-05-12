from django.forms import ModelForm
from .models import *



class TypeForm(ModelForm):
	class Meta:
		model=Type
		fields='__all__'

class ProductForm(ModelForm):
	class Meta:
		model=Product 
		fields='__all__'


class OrderForm(ModelForm):
	class Meta:
		model=Order 
		fields=['address','pincode','mobno']