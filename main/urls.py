from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/',views.contact, name='contact'),
    path('unsubscribe/<str:email>/',views.unsubscribe, name='unsubscribe'),
]
