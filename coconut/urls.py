from django.urls import path
from . import views

urlpatterns = [
    path("/c", views.IndexPage, name="index"),

    path("/m", views.indexPage, name="index"),
]