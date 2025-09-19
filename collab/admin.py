from django.contrib import admin
from .models import CollabRequest


@admin.register(CollabRequest)
class CollabRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_name', 'created_on')
    readonly_fields = ('created_on',)
