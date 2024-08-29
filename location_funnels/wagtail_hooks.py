# myapp/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from .models import LocationPage

class LocationPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Location Pages"
    add_to_admin_menu = True
    model = LocationPage

# Correct the variable name to match the one used in the return statement
location_page_listing_viewset = LocationPageListingViewSet("location_pages")

@hooks.register("register_admin_viewset")
def register_location_page_listing_viewset():
    return location_page_listing_viewset
