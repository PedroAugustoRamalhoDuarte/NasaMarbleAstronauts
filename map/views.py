from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request, template_name)

@csrf_exempt
def get_data(request):
    template_name = 'arduino.html'
    context = {}
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('a0')
        print(data)
        context['a0'] = data
    else:
        context['a0'] = 'irmão manda um POST ae'


    return render(request, template_name, context)

@csrf_exempt
def sensor_log(request):
    return HttpResponse("Hello, you're at sensors4G sensor_log!")