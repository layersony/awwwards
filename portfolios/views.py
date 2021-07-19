from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .models import Profile, Projects, Rate
from .forms import UserForm, ProfileForm, PostForm, RateForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly

from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import ProfileSerializer, ProjectSerializer, UserSerializer
from datetime import date

def index(request):
  allprojects = Projects.objects.all()
  siteday =  Projects.objects.all()
  today_date = date.today()
  return render(request, 'index.html', {'allprojects':allprojects, 'siteday':siteday[:3], 'today_date':today_date})

@login_required(login_url='/accounts/login/')
def profile(request):
  if request.method == 'POST':
    userform = UserForm(request.POST, instance=request.user)
    profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if userform.is_valid and profileform.is_valid():
      userform.save()
      profileform.save()
      messages.success(request, 'Profile updated successfully')
    return redirect('profile')

  userform = UserForm()
  profileform = ProfileForm()
  curr_profile = Profile.objects.get(username = request.user)
  curr_projects = Projects.user_projects(request.user)
  params = {'curr_user': curr_profile, 
            'curr_project': curr_projects,
            'userform':userform,
            'profileform':profileform,
            }
  return render(request, 'profile/index.html', params)

@login_required(login_url='/accounts/login/')
def userprofile(request, id):
  try:
    userdetail = Profile.objects.get(id=id)
    curr_projects = Projects.user_projects(userdetail.username)
    if request.user.username == str(userdetail.username):
      return redirect('profile')
    else:
      return render(request, 'userprofile.html', {'userdetail':userdetail, 'curr_projects':curr_projects})
  except Profile.DoesNotExist:
    return HttpResponseRedirect(', Sorry the Page You Looking For Doesnt Exist.')
    
@login_required(login_url='/accounts/login/')
def postpoject(request):
  if request.method == 'POST':
    postform = PostForm(request.POST, request.FILES)
    if postform.is_valid:
      pro = postform.save(commit=False)
      pro.projectowner = request.user
      pro.save()
    return redirect('profile')

  postform = PostForm()
  params = {'postform':postform,}
  return render(request, 'profile/postproject.html', params)

@login_required(login_url='/accounts/login/')
def projectdetails(request, id):
  specproject = Projects.objects.get(id=id)
  rateform = RateForm()
  allratesproject = Rate.objects.filter(project = specproject.id)
  return render(request, 'profile/projectdetails.html', {'specproject':specproject, 'rateform':rateform, 'allratesproject':allratesproject[:15]})

def search(request):
  if 'search' in request.GET and request.GET['search']:
    search_term = request.GET.get('search')
    searchresults = Projects.searchProjects(search_term)
    return render(request, 'search.html', {'searchresults':searchresults, 'search_term':search_term})
  else:
    return redirect('home')

def ratereview(request):
  design = request.POST.get('design')
  usability = request.POST.get('usability')
  content = request.POST.get('content')
  review = request.POST.get('review')
  project  = Projects.objects.get(id=request.POST.get('project_id'))

  thisRate = Rate.objects.create(design=design, usability=usability, content=content, review=review, project=project, user=request.user )
  allrates = Rate.objects.filter(project=request.POST.get('project_id'))

  design_rates = [d.design for d in allrates]
  design_average = sum(design_rates) / len(design_rates)

  usability_rates = [d.usability for d in allrates]
  usability_average = sum(usability_rates) / len(usability_rates)

  content_rates = [d.content for d in allrates]
  content_average = sum(content_rates) / len(content_rates)

  overall = (design_average + usability_average + content_average)/3

  Rate.objects.filter(id=thisRate.id).update(design_average=round(design_average,2), usability_average=round(usability_average, 2), content_average=round(content_average, 2), overall=round(overall, 2))

  data = {
    'success': 'Review Added Successfully Refresh page for your Review to Appear',
    'design_average': round(design_average, 2),
    'usability_average': round(usability_average, 2),
    'content_average': round(content_average,2),
    'overall': round(overall,2)
    }
  return JsonResponse(data)

class ProfileViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAdminOrReadOnly,)
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAdminOrReadOnly,)
  queryset = Projects.objects.all()
  serializer_class = ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAdminOrReadOnly,)
  queryset = User.objects.all()
  serializer_class = UserSerializer