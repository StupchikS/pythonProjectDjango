from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import Personal

from .models import Personal, Blood, Urea, Patient, MedWork


class PersonalAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Personal
        fields = '__all__'


class PatientAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Patient
        fields = '__all__'


class MedWorkAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = MedWork
        fields = '__all__'


class PersonalAdm(admin.ModelAdmin):
    model = PersonalAdminForm
    list_display = ('id', 'stuff_name', 'fio', 'number_for', 'content', 'photo', 'number_for')
    list_display_links = ('stuff_name', 'fio',)
    search_fields = ('fio',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')

    get_html_photo.short_description = 'фотография если есть'


class PatientAdm(admin.ModelAdmin):
    model = PatientAdminForm
    list_display = ('id', 'patient_number', 'fio', 'data_birthday', 'number_oms', 'adres', 'phone')
    list_display_links = ('patient_number', 'fio')
    search_fields = ('patient_number', 'fio')


class MedWorkAdm(admin.ModelAdmin):
    model = MedWorkAdminForm
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
