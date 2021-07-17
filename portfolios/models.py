from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q


# class projects
class Projects(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to='project/', null=True, blank=True)
  projectowner = models.OneToOneField(User, on_delete=models.CASCADE)
  description = HTMLField(null=True, blank=True)
  livelink = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.title

  def save_project(self):
    self.save()

  @classmethod
  def delete_project(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def update_description(cls, id, description):
    cls.objects.filter(id=id).update(description=description)
  
  @classmethod
  def user_projects(cls, username):
    projects = cls.objects.filter(projectowner__username=username)
    return projects

  @classmethod
  def all_projects(cls):
    allprojects = cls.objects.all()
    return allprojects

  def searchProjects(cls, searchterm):
    searchresults = cls.objects.filter(Q(title__icontains=searchterm) | Q(description__icontains=searchterm) | Q(projectowner__icontains=searchterm))
    return searchresults

# class profile
class Profile(models.Model):
  profilePic = models.ImageField(upload_to='userProfile/', null=True, blank=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = HTMLField(blank=True, null=True)
  email = models.EmailField(blank=True, null=True)
  phone = models.IntegerField(blank=True, null=True)
  count = models.IntegerField(default=0, null=True, blank=True)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(username=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

  def __str__(self):
    return self.username.username
 
# class reviews
class Rate(models.Model):
  design = models.IntegerField(null=True, blank=True, default=0)
  usability = models.IntegerField(null=True, blank=True, default=0)
  content = models.IntegerField(null=True, blank=True, default=0)
  review = models.CharField(max_length=300, blank=True, null=True)
  project = models.ForeignKey(Projects, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.review[:20]

  def save_rate(self):
    self.save()