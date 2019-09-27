from django.urls import include, path
from customers.admin import MyAdminSite, ClientAdmin, PersonAdmin, StatusAdmin, SaleAdmin
from customers.models import Client, Person, Status, Sale

admin_site = MyAdminSite()
admin_site.site_title = 'Sales Application'
admin_site.site_header = 'Sales Application'
admin_site.index_title = 'Menu'
admin_site.register(Client, ClientAdmin)
admin_site.register(Person, PersonAdmin)
admin_site.register(Status, StatusAdmin)
admin_site.register(Sale, SaleAdmin)

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin_site.urls),
    path('customers/', include('customers.urls')),
]
