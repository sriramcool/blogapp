from django.urls import path
from . import views

urlpatterns = [
    path("", views.tech, name="tech"),
    path("explanation/", views.explanation, name = "explanation"),

]