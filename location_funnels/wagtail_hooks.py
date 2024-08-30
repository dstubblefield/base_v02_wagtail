# location_funnels/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from .models import LocationPage  # Ensure LocationPage is a model class

class LocationPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Location Pages"
    add_to_admin_menu = True
    model = LocationPage  # This should be a model class, not a string

location_page_listing_viewset = LocationPageListingViewSet("location_pages")

@hooks.register("register_admin_viewset")
def register_location_page_listing_viewset():
    return location_page_listing_viewset
