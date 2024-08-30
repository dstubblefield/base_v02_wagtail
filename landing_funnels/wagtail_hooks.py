# landing_funnels/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.menu import Menu, SubmenuMenuItem, MenuItem
from wagtail.admin.viewsets.pages import PageListingViewSet

from .models import LandingPage, LandingPageArea, LandingIndexPage


# Define the ViewSets for each Landing Page type
class LandingPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Landing Pages"
    add_to_admin_menu = False  # Set to False because we will add it to a custom menu
    model = LandingPage


class LandingPageAreaListingViewSet(PageListingViewSet):
    icon = "folder"
    menu_label = "Landing Page Areas"
    add_to_admin_menu = False  # We will include this in a custom menu
    model = LandingPageArea


class LandingIndexPageListingViewSet(PageListingViewSet):
    icon = "folder-open-inverse"
    menu_label = "Landing Index Pages"
    add_to_admin_menu = False  # We will include this in a custom menu
    model = LandingIndexPage


# Instantiate the ViewSets
landing_page_listing_viewset = LandingPageListingViewSet("landing_pages")
landing_page_area_listing_viewset = LandingPageAreaListingViewSet("landing_page_areas")
landing_index_page_listing_viewset = LandingIndexPageListingViewSet("landing_index_pages")


@hooks.register("register_admin_viewset")
def register_landing_pages_viewsets():
    return [
        landing_page_listing_viewset,
        landing_page_area_listing_viewset,
        landing_index_page_listing_viewset,
    ]


# Create the custom submenu for Landing Pages
landing_pages_menu = Menu(
    register_hook_name="register_landing_pages_menu",
    construct_hook_name="construct_landing_pages_menu",
)


@hooks.register("construct_landing_pages_menu")
def construct_landing_pages_menu(request, menu_items):
    # Add the individual menu items to the custom landing_pages_menu
    menu_items.append(MenuItem(
        "Landing Pages",
        url="/admin/landing_pages/",
        icon_name="globe",
        classname="icon icon-globe",
        order=100,
    ))
    menu_items.append(MenuItem(
        "Landing Page Areas",
        url="/admin/landing_page_areas/",
        icon_name="folder",
        classname="icon icon-folder",
        order=200,
    ))
    menu_items.append(MenuItem(
        "Landing Index Pages",
        url="/admin/landing_index_pages/",
        icon_name="folder-open-inverse",
        classname="icon icon-folder-open-inverse",
        order=300,
    ))


@hooks.register("register_admin_menu_item")
def register_landing_pages_submenu():
    # Return a SubmenuMenuItem that includes the custom Menu
    return SubmenuMenuItem(
        "Landing Pages",
        landing_pages_menu,
        classname="icon icon-folder-open-inverse",
        order=300,
    )
