from django.contrib import admin

from .models import City, Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code2', 'code3',)
    search_fields = ('name', 'code2', 'code3',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country',)
    search_fields = ('name',)
    raw_id_fields = ('country',)
