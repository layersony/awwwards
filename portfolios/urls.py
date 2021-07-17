from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('account/profile', views.profile, name='profile'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('account/postproject', views.postpoject, name='postproject'),
    path('projectdetails', views.projectdetails, name='projectdetails'),
    path('search/', views.search, name='search')
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  