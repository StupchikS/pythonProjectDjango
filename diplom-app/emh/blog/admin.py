from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import Blog, Index
from django import forms


class IndexAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Index
        fields = '__all__'


class IndexAdmin(admin.ModelAdmin):
    form = IndexAdminForm

    list_display = ('id', 'get_html_photo', 'content')
    list_display_links = ('id', 'content')
    fields = ('content', 'photo')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')

    get_html_photo.short_description = 'Фотография больницы'


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('id', 'title', 'time_created', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    fields = ('title', 'slug', 'content', 'photo', 'is_published', 'time_created', 'time_update')
    readonly_fields = ('get_html_photo', 'time_created', 'time_update')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')

    get_html_photo.short_description = 'миниатюра'


admin.site.register(Blog, BlogAdmin)
admin.site.register(Index, IndexAdmin)

admin.site.site_header = 'Админ панель блога'
admin.site.site_title = 'Админ панель блога'
