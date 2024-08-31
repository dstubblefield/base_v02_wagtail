# flex/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from . models import FlexPage


class FlexPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Flex Pages"
    add_to_admin_menu = True
    model = FlexPage


flex_page_listing_viewset = FlexPageListingViewSet("flex_pages")
@hooks.register("register_admin_viewset")
def register_flex_page_listing_viewset():
    return flex_page_listing_viewset