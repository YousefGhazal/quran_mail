from django.urls import path, include
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('', views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('success/',views.success, name='success'),
    path('unsubscribe/<str:email>/',views.unsubscribe, name='unsubscribe'),
    
]
