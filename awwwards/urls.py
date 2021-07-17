from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolios.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
