from django.shortcuts import render


# view function to get index template
def index(request):
    return render(request, 'index.html')


# view to sentry debug
def sentry_debug(request):
    raise Exception("This is the exception to test Sentry.")
