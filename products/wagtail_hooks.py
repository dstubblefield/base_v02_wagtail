# products/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from . models import ProductPage, ProductsCategoryPage

class ProductsCategoryPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Products Category Page"
    add_to_admin_menu = True
    model = ProductsCategoryPage


products_category_page_listing_viewset = ProductsCategoryPageListingViewSet("products_category_pages")
@hooks.register("register_admin_viewset")
def register_products_category_page_listing_viewset():
    return products_category_page_listing_viewset


class ProductsPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Product Pages"
    add_to_admin_menu = True
    model = ProductPage


products_page_listing_viewset = ProductsPageListingViewSet("products_pages")
@hooks.register("register_admin_viewset")
def register_products_page_listing_viewset():
    return products_page_listing_viewset