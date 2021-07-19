from django import forms
from django.db.models.fields import TextField
from django.forms.fields import ChoiceField
from django.forms.widgets import TextInput
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
    fields = ('title', 'image', 'description', 'livelink',)
    exclude = ['projectowner',]
    widgets = {
        'title':TextInput(attrs={
        'placeholder': 'Project Title...',
      }),
      'livelink': TextInput(attrs={
        'placeholder': 'Project live link...',
      })
    }
  
class RateForm(forms.ModelForm):
  class Meta:
    model = Rate
    fields = ('design', 'usability', 'content', 'review',)
    exclude = ['design_average', 'uability_average', 'content_average', 'project', 'user']
    widgets = {
      'review': TextInput(attrs={
        'class': 'form-control',
        'style': 'max-width:300px',
        'placeholder': 'Reviews...'
      })
    }