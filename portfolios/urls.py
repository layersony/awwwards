from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('projects', views.ProjectViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('account/profile', views.profile, name='profile'),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),
    path('account/postproject', views.postpoject, name='postproject'),
    path('projectdetails/<int:id>/', views.projectdetails, name='projectdetails'),
    path('search/', views.search, name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('ajax/ratereview/', views.ratereview, name='ratereview'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  