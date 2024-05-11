from .models import SimulationData


def clear_data():
    SimulationData.objects.all().delete()

def save_simulation_parameter(parameter_dict):
    new_entry = SimulationData(name=parameter_dict['name'],
                               value=parameter_dict['value'],
                               unit=parameter_dict['unit'])
    new_entry.save()