from django.shortcuts import render
from django.http import HttpResponse
from .models import product, category

#def index(response):
#    #return HttpResponse('<h1> Hi Max! </h1>')
#    return render(response, 'Main2/index.html', {'data': [1,2,3], 'title': 'IndexXXX'})

def index(response):
    data = product.objects.all() 
    return render(response, 'Main2/index.html', {'data': data, 'title':'IndeXXX'})

def Info(response):

    return render(response, 'Main2/info.html')

def test(response):
    data = {'name': 'Product1', 'descr': 'descriptions of the product', 'price': 100}
    return render(response, 'Main2/product.html', data)

def picture(request):
    data = product.objects.all()
    return render(request, 'main2/picture.html',{'data':data})