from django.shortcuts import render
from .forms import MyForm
from .utils import clear_data, save_simulation_parameter


def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            simulation_parameters = [{'name': 'height', 'unit': 'm'},
                                     {'name': 'velocity', 'unit': 'm/s'},
                                     {'name': 'angle', 'unit': 'deg'},
                                     {'name': 'mass', 'unit': 'kg'},
                                     {'name': 'cwArho', 'unit': 'kg/m'},
                                     {'name': 'xmax', 'unit': 'm'},
                                     {'name': 'ymax', 'unit': 'm'},
                                     ]
            clear_data()
            for simulation_parameter_dict in simulation_parameters:
                parameter_name = simulation_parameter_dict['name']
                simulation_parameter_dict['value'] = form.cleaned_data[parameter_name]
                save_simulation_parameter(simulation_parameter_dict)
    else:
        form = MyForm()
    return render(request, 'simulation/index.html', {'form': form})