from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('gallery', views.gallery),
    path('projects', views.projects),
    path('certificates', views.certificates),
    path('contacts', views.contacts),
    path('project2', views.project2),
]