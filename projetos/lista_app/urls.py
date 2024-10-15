# Urls do app
from django.contrib import admin
from django.urls import path
from lista_app import views

urlpatterns = [
    path('', views.index, name="lista"),
    path('del/<str:id_item>', views.remove, name="del"),
    path('admin/', admin.site.urls),
]