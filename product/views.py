from django.shortcuts import render
from django.http import HttpResponse
from .models import AllProduct

def Home(request):
	#return HttpResponse('<h1>Hello KHK</h1>')
	return render(request, 'product/home.html')

def About(request):
	return render(request, 'product/about.html')

def Mobile(request):
	allproduct = AllProduct.objects.all()
	context = {'allproduct':allproduct}
	return render(request, 'product/mobile.html',context)		