from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('info', views.Info, name = 'info'),
    path('product', views.test, name = 'product'),
    path('picture', views.picture, name = 'picture')
]