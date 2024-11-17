from django.shortcuts import render

# Create your views here.

# from netbox.dcim.models import *


from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.db import transaction
from django.db.models import Prefetch
from django.forms import ModelMultipleChoiceField, MultipleHiddenInput, modelformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from jinja2.exceptions import TemplateError



# from circuits.models import Circuit, CircuitTermination
# from extras.views import ObjectConfigContextView
# from ipam.models import ASN, IPAddress, VLANGroup
# from ipam.tables import InterfaceVLANTable
# from netbox.constants import DEFAULT_ACTION_PERMISSIONS
# from netbox.views import generic
# from tenancy.views import ObjectContactsView
# from utilities.forms import ConfirmationForm
# from utilities.paginator import EnhancedPaginator, get_paginate_count
# from utilities.permissions import get_permission_for_model
# from utilities.query import count_related
# from utilities.query_functions import CollateAsChar
# from utilities.views import (
#     GetRelatedModelsMixin, GetReturnURLMixin, ObjectPermissionRequiredMixin, ViewTab, register_model_view
# )
# from virtualization.filtersets import VirtualMachineFilterSet
# from virtualization.forms import VirtualMachineFilterForm
# from virtualization.models import VirtualMachine
# from virtualization.tables import VirtualMachineTable
# from . import filtersets, forms, tables
# from .choices import DeviceFaceChoices, InterfaceModeChoices
# from .models import *



from django.shortcuts import render, get_object_or_404
from .models import SplicePlate, Coupler, Fiber, Module, Cable
# CABLE_TERMINATION_TYPES = {
#     'dcim.consoleport': ConsolePort,
#     'dcim.consoleserverport': ConsoleServerPort,
#     'dcim.powerport': PowerPort,
#     'dcim.poweroutlet': PowerOutlet,
#     'dcim.interface': Interface,
#     'dcim.frontport': FrontPort,
#     'dcim.rearport': RearPort,
#     'dcim.powerfeed': PowerFeed,
#     'circuits.circuittermination': CircuitTermination,
# }
def splice_plate_list(request):
    plates = SplicePlate.objects.all()
    return render(request, 'optic_cable_v1/splice_plate_list.html', {'plates': plates})

def coupler_list(request):
    couplers = Coupler.objects.all()
    return render(request, 'optic_cable_v1/coupler_list.html', {'couplers': couplers})

def fiber_list(request):
    fibers = Fiber.objects.all()
    return render(request, 'optic_cable_v1/fiber_list.html', {'fibers': fibers})

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'optic_cable_v1/module_list.html', {'modules': modules})

def cable_list(request):
    cables = Cable.objects.all()
    return render(request, 'optic_cable_v1/cable_list.html', {'cables': cables})

# class OpticCableTest(generic.ObjectListView):
#     queryset = PowerPort.objects.filter(_path__is_complete=True)
#     filterset = filtersets.PowerConnectionFilterSet
#     filterset_form = forms.PowerConnectionFilterForm
#     table = tables.PowerConnectionTable
#     print("Test OpticCableTest")
#     template_name = 'dcim/connections_list.html'
#     actions = {
#         'export': {'view'},
#     }

#     def get_extra_context(self, request):
#         return {
#             'title': 'Optic cables'
#         }
