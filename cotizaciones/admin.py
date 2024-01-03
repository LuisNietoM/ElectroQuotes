from django.contrib import admin
from .models import Cotizacion


class CotizacionAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_registro']

# Register your models here.
admin.site.register(Cotizacion, CotizacionAdmin)