from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('map/', views.map, name='map'),
    path('shoppinglist/', views.shoppinglist, name='shoppinglist'),
]
