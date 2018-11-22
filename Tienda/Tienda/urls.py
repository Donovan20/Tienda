from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.Productos.urls')),
    path('Productos/', include('apps.Productos.urls')),
]
