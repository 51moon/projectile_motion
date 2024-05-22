from django.shortcuts import render
from .forms import SimulationForm
from .utils import save_simulation_data, simulation

def index(request):
    if request.method == 'POST':
        form = SimulationForm(request.POST)    
        if form.is_valid():
            save_simulation_data(form)
            simulation(request)
    else:
        form = SimulationForm()
    return render(request, 'simulation/index.html', {'form': form})