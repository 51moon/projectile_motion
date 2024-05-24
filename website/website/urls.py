from django.contrib import admin
from django.urls import include, path
from simulation.utils import simulation

urlpatterns = [
    path("", include("simulation.urls")),
    path("admin/", admin.site.urls),
    path('simulation/', simulation, name='simulation'), # trajectory image path
]
