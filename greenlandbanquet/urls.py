from django.contrib import admin
from django.urls import path,include
admin.site.site_header = "Greenland Banquet Admin"
admin.site.site_title = "Greenland Banquet Admin Portal"
admin.site.index_title = "Welcome to Greenland Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('backend.urls'))
]
