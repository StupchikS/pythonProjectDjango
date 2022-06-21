from django.contrib import admin
from .models import Order, StatusCrm, CommentsCrm


class Comment(admin.StackedInline):
    model = CommentsCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 1  # добавляется один доп коммент а не 3 как по умолчанию


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_email', 'order_context', 'order_dt')
    list_display_links = ('id', 'order_name', 'order_context')
    search_fields = ('id', 'order_name', 'order_phone', 'order_email', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_email', 'order_context', 'order_dt')
    readonly_fields = ('id', 'order_dt')
    list_per_page = 10
    list_max_show_all = 50
    inlines = [Comment, ]


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentsCrm)
