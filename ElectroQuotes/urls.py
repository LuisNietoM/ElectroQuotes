
from django.contrib import admin
from django.urls import path
from cotizaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('sign_in/', views.sign_in, name='sign_in'),
]
