from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
    list_display = ('title', 'display_datetime', 'updated_on')
    readonly_fields = ('created_on', 'updated_on')
    fields = ('title', 'content', 'display_datetime', 'created_on', 'updated_on')