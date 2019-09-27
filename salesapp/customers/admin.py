from django.contrib import admin
from .models import Client, Person, Status, Sale
from customers.views import DashboardTemplateView
from django.utils.module_loading import import_string
from django.apps import apps


class MyAdminSite(admin.AdminSite):
    def _setup(self):
        admin_site_class = import_string(apps.get_app_config('admin').default_site)
        self._wrapped = admin_site_class()

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        urls += [
            path('dashboard/', DashboardTemplateView.as_view())
        ]
        return urls


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "tel", "note"]
    search_fields = ["name", "email", "tel"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "client", "email", "tel", "note"]
    search_fields = ["name", "email", "tel"]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "note"]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "person", "date", "status", "note"]
    search_fields = ["name", "client", "status"]
