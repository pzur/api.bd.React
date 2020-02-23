from django.urls import path, include
from .import views
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register('servicioscliente',views.ClienteList)


urlpatterns = [
    path('',include(routers.urls))
    #path('', views.list_all_servicios_json,name='list_all_servicios'),
]