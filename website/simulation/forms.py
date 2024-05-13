from django import forms

class MyForm(forms.Form):
    height = forms.FloatField(label='Height', initial=1)
    velocity = forms.FloatField(label='Velocity', initial=20)
    angle = forms.FloatField(label='Angle', initial=40)
    mass = forms.FloatField(label='Mass', initial=1)
    cwArho = forms.FloatField(label='Friction Factor', initial=1)
    xmax = forms.FloatField(label='x-range', initial=6)
    ymax = forms.FloatField(label='y-range', initial=4)