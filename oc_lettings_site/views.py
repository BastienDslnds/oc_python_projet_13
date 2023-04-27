from django.shortcuts import render
from .models import Letting, Profile


# view function to get index template
def index(request):
    return render(request, 'index.html')


# view function to get list of lettings
def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


# view function to get a specific letting
def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)


# view function to get a list of profiles
def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


# view function to get a specific profile
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
