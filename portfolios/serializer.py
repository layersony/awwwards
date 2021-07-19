from rest_framework import serializers
from .models import Profile, Projects
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ('id', 'title', 'image', 'projectowner', 'description', 'livelink', 'url')

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile 
    fields = ('id', 'username', 'profilePic', 'bio', 'phone', 'url')

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only=True)
  projects = ProjectSerializer(read_only=True, many=True)

  class Meta:
    model = User
    fields = ['id', 'url', 'username', 'profile', 'projects']