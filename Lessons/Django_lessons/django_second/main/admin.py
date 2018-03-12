from django.contrib import admin
from .models import Page


class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "surname", "name", "about", "mass", "birth")
    list_editable = ("surname", "name", "mass", "birth")
    list_display_links = ("name",)
    search_fields = ("name", "surname")


admin.site.register(Page, PersonAdmin)
