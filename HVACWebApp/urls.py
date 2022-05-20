
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('HVACtodo/', include('HVACtodo.urls')),
    path('admin/', admin.site.urls),
]