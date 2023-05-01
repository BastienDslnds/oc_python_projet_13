from django.shortcuts import render


# view function to get index template
def index(request):
    return render(request, 'index.html')
