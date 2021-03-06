from inspect import formatargspec
from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_file,name='create_file'),
    path('List/', views.File_list, name='File.List'),
    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'),
    path('ajax/load-sections/', views.load_sections, name='ajax_load_sections'),
    path('pdf<int:id>/', views.GeneratePdf, name='File_pdf_print'),
]