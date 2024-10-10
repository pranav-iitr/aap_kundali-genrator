from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import House, DashaPhal, AntarDashaPhal,PratyantarDashaPhal

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_no', 'rashi', 'surya_present', 'moon_present', 'surya_drishti', 'moon_drishti')
    list_filter = ('rashi', 'surya_present', 'moon_present', 'surya_drishti', 'moon_drishti')
    search_fields = ('house_no', 'rashi')

@admin.register(DashaPhal)
class DashaPhalAdmin(admin.ModelAdmin):
    list_display = ('planet', )
    search_fields = ('planet', )

@admin.register(AntarDashaPhal)
class AntarDashaPhalAdmin(admin.ModelAdmin):
    list_display = ('dasha', 'planet')
    search_fields = ('dasha', 'planet')

@admin.register(PratyantarDashaPhal)
class PratyantarDashaPhalAdmin(admin.ModelAdmin):
    list_display = ('antardasha', 'planet')
    search_fields = ('antardasha', 'planet')