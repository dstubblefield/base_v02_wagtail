# app_forms/forms.py

from django import forms
from wagtail.admin.forms import WagtailAdminPageForm
from .mixins import OrderedCountyMixin

class GenericStaffForm(OrderedCountyMixin, WagtailAdminPageForm):
    pass
