# faq/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet
from .models import FaqPage

class FaqPageListingViewSet(PageListingViewSet):
    icon = "help"
    menu_label = "FAQ Page"
    add_to_admin_menu = True
    model = FaqPage

# Instantiate the viewset
faq_page_listing_viewset = FaqPageListingViewSet("faq_pages")

@hooks.register("register_admin_viewset")
def register_faq_page_listing_viewset():
    return faq_page_listing_viewset  # Return the instance of the viewset

