from django.urls import path

from api.views.config_view import ConfigView

urlpatterns = [

    path("config", ConfigView.as_view()),

]