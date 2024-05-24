from django.shortcuts import render
from .forms import SimulationForm
from .models import SimulationData
from .utils import simulation

def index(request):
    initial_data = SimulationData.objects.first()
    if request.method == 'POST':
        form = SimulationForm(request.POST, instance=initial_data)
        if form.is_valid():
            form.save()
            simulation(request)
    else:
        form = SimulationForm(instance=initial_data)
    return render(request, 'simulation/index.html', {'form': form})