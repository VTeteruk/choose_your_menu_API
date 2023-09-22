from django.contrib import admin
from .models import Menu, Restaurant


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'date')
    list_filter = ('restaurant',)
    search_fields = ('restaurant__name', 'date')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
