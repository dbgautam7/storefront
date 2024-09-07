from django.urls import path
from . import views

# URL configuration for storefront project.
urlpatterns = [path("hello/", views.say_hello)]
