from django.test import TestCase
from .models import Projects, Profile, Rate
from django.contrib.auth.models import User

class TestProjects(TestCase):
  def setUp(self):
    self.newproject = Projects(title='Delani Studion', image='test.jpg', projectowner= User.objects.create(username='layersony'), description='a clone for delani studio', livelink='http://google.com/?search=this+is+amazing')
    self.newproject.save_project()

  def teardown(self):
    User.objects.all().delete()
    Projects.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.newproject, Projects))

# Create your tests here.
