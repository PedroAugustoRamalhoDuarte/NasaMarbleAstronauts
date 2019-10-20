from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Arduino
# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

@csrf_exempt
def get_data(request):
    template_name = 'arduino.html'
    context = {}
    if request.method == 'POST':
        a0 = request.POST.get('a0')
        a1 = request.POST.get('a1')
        a2 = request.POST.get('a2')
        context['a0'] = a0
        context['a1'] = a1
        context['a2'] = a2

    else:
        context['a0'] = 'irmão manda um POST ae'
        context['data'] = Arduino.objects.all()

    return render(request, template_name, context)

@csrf_exempt
def sensor_log(request):
    return HttpResponse("Hello, you're at sensors4G sensor_log!")