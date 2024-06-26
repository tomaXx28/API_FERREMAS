"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from api import views
from api.views import Cliente , Producto, ProductoDetailView , TipoProducto, DetalleCliente, DetalleProducto


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/',include ('api.urls')),
    path ('docs/',include_docs_urls(title='Api Documentantion')),
    path('cliente/', views.ClienteViewset.as_view({'get': 'list', 'post': 'create'}), name='cliente-list'),
    path('cliente/<int:idCliente>/', DetalleCliente.as_view(), name='cliente-detail'),
    path('producto/', views.ProductoViewset.as_view({'get': 'list', 'post': 'create'}), name='producto-list'),
    path('tipoproducto/', views.TipoProductoViewset.as_view({'get': 'list', 'post': 'create'}), name='tipo-producto-list'),
    path('productos_por_tipo/', views.productos_por_tipo, name='productos_por_tipo'),
     path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('tipoproducto/<int:idTipo>/', views.TipoProductoViewset.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='tipo-producto-detail'),
    path('producto/<int:id>/', ProductoDetailView.as_view(), name='producto-detail'),
]
