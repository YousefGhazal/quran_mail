from django.urls import path, include
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
]
