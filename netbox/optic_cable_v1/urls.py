from django.urls import include, path
from . import views

from netbox.utilities.urls import get_model_urls





# urlpatterns = [
#     path('splice-plates/', views.splice_plate_list, name='splice_plate_list'),
#     path('couplers/', views.coupler_list, name='coupler_list'),
# ]



from django.urls import path
from . import views


app_name = 'optic_cable_v2'

urlpatterns = [
    path('splice-plates/', views.splice_plate_list, name='splice_plate_list'),
    path('couplers/', views.coupler_list, name='coupler_list'),
    path('fibers/', views.fiber_list, name='fiber_list'),
    path('modules/', views.module_list, name='module_list'),
    path('cables/', views.cable_list, name='cable_list'),
]
