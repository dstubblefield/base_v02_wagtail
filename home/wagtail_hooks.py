# flex/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from . models import HomePage


class HomePageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Home Page"
    add_to_admin_menu = True
    model = HomePage


home_page_listing_viewset = HomePageListingViewSet("home_pages")
@hooks.register("register_admin_viewset")
def register_home_page_listing_viewset():
    return home_page_listing_viewset