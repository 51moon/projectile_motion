import math
import matplotlib.pyplot as plt
import numpy as np
import scipy
from django.http import HttpResponse
from io import BytesIO
from .models import SimulationData


def get_simulation_parameters_template():
    simulation_parameters = [{'name': 'height', 'unit': 'm'},
                             {'name': 'velocity', 'unit': 'm/s'},
                             {'name': 'angle', 'unit': '°'},
                             {'name': 'mass', 'unit': 'kg'},
                             {'name': 'cwArho', 'unit': 'kg/m'},
                             {'name': 'xmax', 'unit': 'm'},
                             {'name': 'ymax', 'unit': 'm'},
                            ]
    return simulation_parameters


def clear_data():
    SimulationData.objects.all().delete()


def save_simulation_parameter(parameter_dict):
    new_entry = SimulationData(name=parameter_dict['name'],
                               value=parameter_dict['value'],
                               unit=parameter_dict['unit'])
    new_entry.save()
    
    
def load_simulation_parameters():
    simulation_parameters_template = get_simulation_parameters_template()
    all_entries = SimulationData.objects.all().order_by('-id')[:len(simulation_parameters_template)]
    simulation_parameters = dict()
    for entry in all_entries:
        simulation_parameters[entry.name] = entry.value
    return simulation_parameters
    
    
def simulation(request):
    simulation_parameters = load_simulation_parameters()
        
    # Read the parameters from the input fields.
    height = simulation_parameters['height']
    velocity = simulation_parameters['velocity']
    angle = math.radians(simulation_parameters['angle'])
    mass = simulation_parameters['mass']
    cwArho = simulation_parameters['cwArho']
    xmax = simulation_parameters['xmax']
    ymax = simulation_parameters['ymax']

    # Constants
    g = 9.807

    # Set the initial state vector at time t=0.
    r0 = np.array([0, height])
    v0 = velocity * np.array([math.cos(angle), math.sin(angle)])
    u0 = np.concatenate((r0, v0))

    def differential_eq(t, u):
        """Calculate the right-hand side of the differential equation."""
        r, v = np.split(u, 2)
        # Air friction force.
        Fr = -0.5 * cwArho * np.linalg.norm(v) * v
        # Gravity force.
        Fg = mass * g * np.array([0, -1])
        # Acceleration.
        a = (Fr + Fg) / mass
        return np.concatenate([v, a])

    def collision(t, u):
        """Event function: Detect the collision."""
        r, v = np.split(u, 2)
        return r[1]

    # Terminate integration upon collision with the ground.
    collision.terminal = True
    collision.direction = -1

    # Solve the motion equation.
    result = scipy.integrate.solve_ivp(differential_eq, [0, np.inf], u0,
                                        events=collision,
                                        dense_output=True)

    # Calculate interpolation on a fine grid.
    t = np.linspace(0, np.max(result.t), 1000)
    r, v = np.split(result.sol(t), 2)

    # Generate plot.
    x = r[0]
    y = r[1]

    px = 1/plt.rcParams['figure.dpi']
    plt.figure(figsize=(600*px, 450*px))
    plt.plot(x, y)
    plt.title('Trajectory')
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.tight_layout()

    # Save image as BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='jpg')
    buffer.seek(0)
    plt.close()
    
    return HttpResponse(buffer.getvalue(), content_type='image/jpeg')