from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy


from emh.utils import DataMixin
from django.views.generic import ListView, CreateView

from .forms import GetInfoForm
from .models import Personal


class Person(DataMixin, ListView):

    model = Personal
    template_name = 'medbase/person.html'
    context_object_name = 'person'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Администрация больницы')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Personal.objects.all()


def getinfo(request):
    form = GetInfoForm()

    dict_obj = {

        'form': form,
    }
    return render(request, 'medbase/getinfo.html', dict_obj)


def patient_info(request):
    if request.POST:
        number = request.POST['number']
        birthday = request.POST['birthday']
        oms = request.POST['oms']
        return render(request, 'medbase/patient_info.html', {'name': number, 'birthday': birthday, 'oms': oms})
    else:
        return render(request, 'medbase/patient_info.html')


