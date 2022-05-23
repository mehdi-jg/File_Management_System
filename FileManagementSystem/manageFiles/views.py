from django.shortcuts import render
from django.http import HttpResponse
from .form import FileForm
def index(request):

    form = FileForm()

    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'X/form.html', context)
   

def new_func(request):
    return render(request, 'index.html')

