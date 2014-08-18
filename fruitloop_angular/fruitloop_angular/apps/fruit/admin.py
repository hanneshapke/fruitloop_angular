from django.contrib.gis import admin
from .models import FruitLocation, FruitType


class FruitLocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 11
    list_display = (
        'fruit_type', 'address',
        'modified',)


admin.site.register(FruitLocation, FruitLocationAdmin)
admin.site.register(FruitType)
