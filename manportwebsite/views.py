from django.shortcuts import render




def home(request):
	return render(request, 'home.html', {})


def project(request):
	return render(request, 'project.html', {})


# Create your views here.
