from django.urls import path

from . import views

app_name = "asu"
urlpatterns = [
    path("", views.index, name="index"),
]
