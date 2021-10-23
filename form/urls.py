from django.contrib import admin
from django.urls import path
from form import views

urlpatterns = [
    path("", views.index, name='form'),
    path("contact", views.index, name='contact')
]
