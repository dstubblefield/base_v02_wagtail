# blog/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from . models import BlogDetail


class BlogPageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Blog Posts"
    add_to_admin_menu = True
    model = BlogDetail


blog_page_listing_viewset = BlogPageListingViewSet("blog_pages")
@hooks.register("register_admin_viewset")
def register_blog_page_listing_viewset():
    return blog_page_listing_viewset