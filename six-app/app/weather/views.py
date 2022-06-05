from django.shortcuts import render

def weather(request):
    return render(request, template_name='weather/weather.html')
