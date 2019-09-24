from django.contrib import admin
from .models import Client, Person, Status, Sale


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "tel", "note"]
    search_fields = ["name", "email", "tel"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "tel", "note"]
    search_fields = ["name", "email", "tel"]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "note"]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "client", "date", "status", "note"]
    search_fields = ["name", "client", "status"]
