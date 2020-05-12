from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def base(response):
	return render(response,'main/base1.html')



def register(response):
	if response.method=='POST':
		form=UserCreationForm(response.POST)
		if form.is_valid():
			form.save()
	else:
		form=UserCreationForm()
	return render(response,'main/register.html',{'form':form})




def products(response):
	items=Type.objects.filter(category='Electronics')
	items=Product.objects.filter(category=items[0])
	items1=Type.objects.all()
	return render(response,'main/products.html',{'items':items,'items1':items1})




def additems(response):
	if response.method=='POST':
		form=ProductForm(response.POST,response.FILES)
		if form.is_valid():
			form.save()
	else:
		form=ProductForm()
	return render(response,'main/additems.html',{'form':form})



def addtype(response):
	if response.method=='POST':
		form=TypeForm(response.POST)
		if form.is_valid():
			form.save()
	else:
		form=TypeForm()
	return render(response,'main/addtype.html',{'form':form})




@login_required(login_url='/login/')
def addcart(response,id):
	new=Product.objects.filter(id=id)
	if not Cart.objects.filter(li=new[0],name=response.user,user=response.user).exists():
		temp=Cart(li=new[0],name=response.user,user=response.user)
		temp.save()
	return redirect('products')




@login_required(login_url='/login/')
def showcart(response):
	data=Product.objects.filter(cart__user=response.user)
	return render(response,'main/showcart.html',{'data':data})




@login_required(login_url='/login/')
def deletecart(response,name):
	name=Product.objects.filter(name=name)
	temp=Cart.objects.filter(li=name[0])
	temp.delete()
	return redirect('showcart')




def category(response,category):
	items=Type.objects.filter(category=category)
	items=Product.objects.filter(category=items[0])
	items1=Type.objects.all()
	return render(response,'main/products.html',{'items':items,'items1':items1})




@login_required(login_url='/login/')
def deleteitem(response,id):
	new=Product.objects.filter(id=id)
	new.delete()
	return redirect('products')




@login_required(login_url='/login/')
def allorder(response):
	data=Cart.objects.filter(user=response.user)
	if response.method=='POST':
		form=OrderForm(response.POST)
		if form.is_valid():
			temp=form.save(commit=False)
			temp.li=response.user
			temp.save()
			for i in data:
				temp.cart.add(i)
			
	else:
		form=OrderForm()
	return render(response,'main/allorder.html',{'form':form})




@login_required(login_url='/login')
def oneorder(response,id):
	temp=Product.objects.filter(id=id)
	if response.method=='POST':
		form=OrderForm(response.POST)
		if form.is_valid():
			new=form.save(commit=False)
			new.li=response.user
			new.product=temp[0]
			new.save()
	else:
		form=OrderForm()
	return render(response,'main/allorder.html',{'form':form})


def showproduct(response,id):
	data=Product.objects.filter(id=id)
	return render(response,'main/showproduct.html',{'data':data})
