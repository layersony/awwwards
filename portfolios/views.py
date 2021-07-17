from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects, Rate
from .forms import UserForm, ProfileForm, PostForm
from django.contrib import messages

def index(request):
  allprojects = Projects.objects.all()
  return render(request, 'index.html', {'allprojects':allprojects})

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
def userprofile(request):
  return render(request, 'userprofile.html')

@login_required(login_url='/accounts/login/')
def postpoject(request):
  if request.method == 'POST':
    postform = PostForm(request.POST, request.FILES, instance=request.user.profile)
    if postform.is_valid:
      pro = postform.save(commit=False)
      pro.projectowner = request.user
      pro.save()
      return redirect('profile')

  postform = PostForm()
  params = {'postform':postform,}
  return render(request, 'profile/postproject.html', params)

def projectdetails(request):
  return render(request, 'profile/projectdetails.html')

def search(request):
  return render(request, 'search.html')