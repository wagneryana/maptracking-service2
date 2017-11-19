from django.contrib import admin
from maptracking.models_raiz import Producto
from maptracking.models_raiz import UnidadMed
from maptracking.models.categoria import Categoria
from maptracking.models_raiz import Venta, ShoppingCart, Cliente
from maptracking.models.animal import Animal
from maptracking.models.carrera import Carrera
from maptracking.models.catalgo_perfil import Catalogo_perfil
from maptracking.models.competencia_general import Competencia_general
from maptracking.models.escuela import Escuela
from maptracking.models.perfil import Perfil
from maptracking.models.unidad_competencia import Unidad_competencia

# Register your models here.


admin.site.register(UnidadMed)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(ShoppingCart)
admin.site.register(Venta)
admin.site.register(Animal)
admin.site.register(Carrera)
admin.site.register(Catalogo_perfil)
admin.site.register(Competencia_general)
admin.site.register(Escuela)
admin.site.register(Perfil)
admin.site.register(Unidad_competencia)


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
