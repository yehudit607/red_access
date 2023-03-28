from django.urls import path

from .views.redis import health_check


urlpatterns = [
    #Redis
    path("health_check", health_check)
]
