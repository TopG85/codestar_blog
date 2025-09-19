from django.urls import path
from . import views

app_name = 'collab'

urlpatterns = [
    path('request/', views.request_collab, name='request'),
]
