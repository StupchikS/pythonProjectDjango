from django.shortcuts import render
from .models import ElectricCarDir


def index(request):
    projects = ElectricCarDir.objects.all()
    return render(request, 'electric_car_dir/index.html', {'projects': projects})
