from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def get_data(request):
    return HttpResponse("Hello, you're at the sensors4G index!")

@csrf_exempt
def sensor_log(request):
    return HttpResponse("Hello, you're at sensors4G sensor_log!")