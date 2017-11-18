from django.contrib import admin
from maptracking.models_raiz import Producto
from maptracking.models_raiz import UnidadMed
from maptracking.models.categoria import Categoria
from maptracking.models_raiz import Venta, ShoppingCart, Cliente
from maptracking.models.animal import Animal
# Register your models here.


admin.site.register(UnidadMed)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(ShoppingCart)
admin.site.register(Venta)
admin.site.register(Animal)


class ProductoAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_per_page = 2
    list_display = ("codigo", "nombre",
                    "unidad_med_codigo", "categorias")
    search_fields = ("codigo", "nombre",)

    def unidad_med_codigo(self, obj):
        return obj.unidad_med.codigo

    def categorias(self, obj):
        return obj.categoria.all()

admin.site.register(Producto, ProductoAdmin)
