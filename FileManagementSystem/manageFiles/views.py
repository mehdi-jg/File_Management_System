from django.shortcuts import render

from manageFiles.models import JGDepartment, JGDivision, JGSection
from .forms import FileForm
from django.http import HttpResponseBadRequest

def index(request):

    form = FileForm()

    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'X/form_add_new_file.html', context)
   

def new_func(request):
    return render(request, 'index.html')


def load_departments(request):
    division_id = request.GET.get('file_division')
    departments = JGDepartment.objects.filter(JGDivision_id=division_id).order_by('NothiCode')
    return render(request, 'X/departments_dropdown_list_options.html', {'departments': departments})

def load_sections(request):
    department_id = request.GET.get('file_department')
    sections = JGSection.objects.filter(JGDepartment=department_id).order_by('NothiCode')
    return render(request, 'X/sections_dropdown_list_options.html', {'sections': sections})
