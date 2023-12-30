
from django.contrib import admin
from django.urls import path
from cotizaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]
