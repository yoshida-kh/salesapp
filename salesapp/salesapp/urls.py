from django.urls import include, path
from customers.admin import MyAdminSite
from customers.models import Client, Person, Status, Sale

admin_site = MyAdminSite()
admin_site.site_title = 'Sales Application'
admin_site.site_header = 'Sales Application'
admin_site.index_title = 'Menu'
admin_site.register([Client, Person, Status, Sale])

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin_site.urls),
    path('customers/', include('customers.urls')),
]
