from django.contrib import admin
from .models import Mask, SurgicalCap, CustomOrder


# Register your models here.

@admin.register(Mask)
class MaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name',)

@admin.register(SurgicalCap)
class SurgicalCapAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name',)

@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'custom_text', 'order_date')
    search_fields = ('product_type', 'custom_text')