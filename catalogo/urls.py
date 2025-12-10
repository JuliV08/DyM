from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.producto_list, name='producto_list'),
    path('producto/<slug:slug>/', views.producto_detail, name='producto_detail'),
    path('marcas/', views.marca_list, name='marca_list'),
    path('marca/<slug:slug>/', views.marca_detail, name='marca_detail'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
