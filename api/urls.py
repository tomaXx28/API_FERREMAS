from django.urls import path, include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewset)
router.register(r'productos', views.ProductoViewset)
router.register(r'tipoproductos', views.TipoProductoViewset)

urlpatterns= [
    path('',include(router.urls))
]

