from django import forms
from .models import Projects, Profile, Rate
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email',)

class ProfileForm(forms.ModelForm):
    class Meta:
      model = Profile
      fields = '__all__'
      exclude = ['username', 'count',]

class PostForm(forms.ModelForm):
  class Meta:
    model = Projects
    fields = '__all__'
    exclude = ['projectowner',]