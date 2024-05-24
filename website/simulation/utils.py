import math
import matplotlib.pyplot as plt
import numpy as np
import scipy
from django.http import HttpResponse
from io import BytesIO
from .models import SimulationData

def save_simulation_data(form):
    new_simulation_data = SimulationData()
    # Populate the new instance with form data
    new_simulation_data.height = form.cleaned_data['height']
    new_simulation_data.velocity = form.cleaned_data['velocity']
    new_simulation_data.angle = form.cleaned_data['angle']
    new_simulation_data.mass = form.cleaned_data['mass']
    new_simulation_data.cwArho = form.cleaned_data['cwArho']
    new_simulation_data.xmax = form.cleaned_data['xmax']
    new_simulation_data.ymax = form.cleaned_data['ymax']
    # Save the new instance
    new_simulation_data.save()

def simulation(request):
    simulation_data = SimulationData.objects.first()
        
    # Constants
    g = 9.807

    # Set the initial state vector at time t=0.
    r0 = np.array([0, simulation_data.height])
    angle = math.radians(simulation_data.angle)
    v0 = simulation_data.velocity * np.array([math.cos(angle), math.sin(angle)])
    u0 = np.concatenate((r0, v0))

    def differential_eq(t, u):
        """Calculate the right-hand side of the differential equation."""
        r, v = np.split(u, 2)
        # Air friction force.
        Fr = -0.5 * simulation_data.cwArho * np.linalg.norm(v) * v
        # Gravity force.
        Fg = simulation_data.mass * g * np.array([0, -1])
        # Acceleration.
        a = (Fr + Fg) / simulation_data.mass
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
    plt.xlim(0, simulation_data.xmax)
    plt.ylim(0, simulation_data.ymax)
    plt.grid(True)
    plt.tight_layout()

    # Save image as BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='jpeg')
    buffer.seek(0)
    plt.close()
    
    return HttpResponse(buffer.getvalue(), content_type='image/jpeg')