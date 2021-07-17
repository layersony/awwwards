from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('account/profile', views.profile, name='profile'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('account/postproject', views.postpoject, name='postproject'),
    path('projectdetails', views.projectdetails, name='projectdetails'),
    path('search/', views.search, name='search')
]
