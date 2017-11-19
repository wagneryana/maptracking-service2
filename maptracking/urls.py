from django.conf.urls import url, include
from rest_framework import routers
from .views.categoria_view import CategoriaViewSet
from .views.facultad_view import FacultadViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'facultades', FacultadViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
