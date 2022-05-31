from inspect import formatargspec
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'),
    path('ajax/load-sections/', views.load_sections, name='ajax_load_sections'),
]