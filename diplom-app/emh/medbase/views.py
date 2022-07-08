from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from emh.utils import DataMixin
from django.views.generic import ListView, CreateView

from .forms import GetInfoForm
from .models import *


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

    # dict_obj = {
    #
    #     'form': form,
    # }
    return render(request, 'medbase/getinfo.html',
                  {'number': form['number'], 'birthday': form['birthday'], 'oms': form['oms']})


def patient_info(request):
    if request.POST:
        number = request.POST['number']
        birthday = request.POST['birthday']
        oms = request.POST['oms']
        select_bd = request.POST['select_bd']
        patient = Patient.objects.filter(patient_number=number, number_oms=oms, data_birthday=birthday)
        if patient:
            if select_bd == "blood":
                blood = Blood.objects.all()
                return render(request, 'medbase/patient_info.html',
                              {'title': f'Анализы крови пациента № {number}', 'blood': blood, 'patient': patient})
            elif select_bd == "urea":
                urea = Urea.objects.all()
                return render(request, 'medbase/patient_info.html',
                              {'title': f'Анализы мочи пациента № {number}', 'urea': urea, 'patient': patient})
            elif select_bd == "medwork":
                medwork = MedWork.objects.all()
                return render(request, 'medbase/patient_info.html',
                              {'title': f'Информация о приемах пациента № {number}', 'medwork': medwork,
                               'patient': patient})
        else:
            return render(request, 'medbase/patient_info.html', {'title': "Данные введены не правильно"})
        # dict_form = {
        #     'title': f'Информация о пациенте № {number}',
        #     'select_bd': select_bd,
        #     'name': number,
        #     'birthday': birthday,
        #     'oms': oms
        # }
        #
        # return render(request, 'medbase/patient_info.html', dict_form)

    else:
        return render(request, 'medbase/getinfo.html')
