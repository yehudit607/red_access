from django.urls import path
from .views import scan_file_view

urlpatterns = [
    path('scan', scan_file_view, name='scan_file'),
]