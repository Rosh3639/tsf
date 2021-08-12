
from django.urls import path
from tsfpayment import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('contact', views.contact, name='Contact'),
    path('about', views.about, name='About'),
]