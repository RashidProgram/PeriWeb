from django.contrib import admin
from .models import Products, Catalog, Options


class OptionInline(admin.TabularInline):
    model = Options


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    inlines = [OptionInline, ]


admin.site.register(Products, ProductAdmin)
admin.site.register(Catalog)

