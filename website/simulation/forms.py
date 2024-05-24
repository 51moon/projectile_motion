from django import forms
from .models import SimulationData

class SimulationForm(forms.ModelForm):
    class Meta:
        model = SimulationData
        fields = ['height', 'velocity', 'angle', 'mass', 'c_F', 'xmax', 'ymax']