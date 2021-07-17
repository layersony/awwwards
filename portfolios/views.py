from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def profile(request):
  return render(request, 'profile/index.html')

def userprofile(request):
  return render(request, 'userprofile.html')

def postpoject(request):
  return render(request, 'profile/postproject.html')

def projectdetails(request):
  return render(request, 'profile/projectdetails.html')

def search(request):
  return render(request, 'search.html')