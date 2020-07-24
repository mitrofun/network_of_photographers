from django.contrib import admin

from .models import Thing, ThingInCity, ThingInUse


class ThingInCityInLineAdmin(admin.TabularInline):
    model = ThingInCity
    extra = 1


class ThingInUseInLineAdmin(admin.TabularInline):
    model = ThingInUse
    extra = 1


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    inlines = (ThingInCityInLineAdmin, ThingInUseInLineAdmin,)
