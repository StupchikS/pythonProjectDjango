from django.contrib import admin
from .models import Personal, Blood, Urea, Patient, MedWork


class PersonalAdm(admin.ModelAdmin):
    model = Personal
    list_display = ('id', 'stuff_name', 'fio', 'number_for', 'content', 'photo', 'number_for')
    list_display_links = ('stuff_name', 'fio',)
    search_fields = ('fio',)


class PatientAdm(admin.ModelAdmin):
    model = Patient
    list_display = ('id', 'patient_number', 'fio', 'data_birthday', 'number_oms', 'adres', 'phone')
    list_display_links = ('patient_number', 'fio')
    search_fields = ('patient_number', 'fio')


class MedWorkAdm(admin.ModelAdmin):
    model = MedWork
    list_display = ('patient_number', 'data_work', 'content_work', 'recomend_work')
    list_display_links = ('patient_number', 'data_work')
    search_fields = ('patient_number',)


class BloodAdm(admin.ModelAdmin):
    model = Blood
    list_display = ('patient_number', 'data_work', 'belock', 'hgb', 'sugar', 'text_blood')
    list_display_links = ('patient_number', 'data_work')
    search_fields = ('patient_number',)


class UreaAdm(admin.ModelAdmin):
    model = Urea
    list_display = ('patient_number', 'data_work', 'belock', 'sugar', 'mochevina', 'text_urea')
    list_display_links = ('patient_number', 'data_work')
    search_fields = ('patient_number',)


admin.site.register(Personal, PersonalAdm)
admin.site.register(Patient, PatientAdm)
admin.site.register(MedWork, MedWorkAdm)
admin.site.register(Blood, BloodAdm)
admin.site.register(Urea, UreaAdm)
