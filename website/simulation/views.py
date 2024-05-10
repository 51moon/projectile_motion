from django.shortcuts import render
from .forms import MyForm


def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            velocity = form.cleaned_data['velocity']
            angle = form.cleaned_data['angle']
            mass = form.cleaned_data['mass']
            cwArho = form.cleaned_data['cwArho']
            xmax = form.cleaned_data['xmax']
            ymax = form.cleaned_data['ymax']
        
    else:
        form = MyForm()
    return render(request, 'simulation/index.html', {'form': form})