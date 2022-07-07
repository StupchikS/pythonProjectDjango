from django.shortcuts import render

from emh.utils import DataMixin
from django.views.generic import ListView
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
