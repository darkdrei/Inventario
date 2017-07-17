from django.conf.urls import url
import views


# url ws de tipo de servicios porvehiculo
urlpatterns = [
    url(r'^ws/articulos/proveedor/$', views.ListArtProveedor.as_view(), name='ws_articulo_proveedor'),
]
