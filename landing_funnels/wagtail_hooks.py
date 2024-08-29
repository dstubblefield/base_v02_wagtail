# myapp/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from . models import  LandingPage


class  LandingPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = " Landing Pages"
    add_to_admin_menu = True
    model =  LandingPage


landing_page_listing_viewset = LandingPageListingViewSet("landing_pages")
@hooks.register("register_admin_viewset")
def register_landing_page_listing_viewset():
    return landing_page_listing_viewset