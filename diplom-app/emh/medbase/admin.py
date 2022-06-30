from django.contrib import admin
from .models import Personal


class PersonalAdm(admin.ModelAdmin):
    model = Personal
    list_display = ('id', 'stuff_name', 'fio', 'number_for', 'content', 'photo', 'number_for')
    list_display_links = ('stuff_name', 'fio',)
    search_fields = ('fio',)




admin.site.register(Personal, PersonalAdm)
