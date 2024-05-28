from django.contrib import admin
from .models import Cliente
from .models import Producto
from .models import TipoProducto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(TipoProducto)

 