from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# class projects
class Projects(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to='project/', null=True, blank=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  description = HTMLField(null=True, blank=True)
  livelink = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.title

# class profile

# class reviews