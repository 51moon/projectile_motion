from django.shortcuts import render
from .forms import MyForm
from .utils import clear_data, save_simulation_parameter, get_simulation_parameters_template, simulation


def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            clear_data()
            for simulation_parameter_dict in get_simulation_parameters_template():
                parameter_name = simulation_parameter_dict['name']
                simulation_parameter_dict['value'] = form.cleaned_data[parameter_name]
                save_simulation_parameter(simulation_parameter_dict)
            simulation(request)
    else:
        form = MyForm()
    return render(request, 'simulation/index.html', {'form': form})