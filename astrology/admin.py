from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_no', 'rashi', 'surya_present', 'moon_present', 'surya_drishti', 'moon_drishti')
    list_filter = ('rashi', 'surya_present', 'moon_present', 'surya_drishti', 'moon_drishti')
    search_fields = ('house_no', 'rashi')