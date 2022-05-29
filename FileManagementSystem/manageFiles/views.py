from django.shortcuts import render
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

