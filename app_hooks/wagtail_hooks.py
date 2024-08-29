# admin_hooks/wagtail_hooks.py

from wagtail import hooks
from django.templatetags.static import static
from django.utils.html import format_html

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/custom_admin.css'))

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from taggit.models import Tag
from app_snippets.models import Author, County, City
from wagtail.models import Page
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from django.utils.translation import gettext_lazy as _
from wagtail.admin.menu import Menu, SubmenuMenuItem, MenuItem

from wagtail.images.wagtail_hooks import register_images_menu_item
from wagtail.documents.wagtail_hooks import register_documents_menu_item
from wagtail.admin.wagtail_hooks import register_collections_menu_item

# change app to your main app folder with settings/base.py
from core.settings.base import HIDDEN_SETTINGS_MENU_ITEMS, HIDDEN_MAIN_MENU_ITEMS

assets_menu = Menu(
    register_hook_name="register_assets_menu",
    construct_hook_name="construct_assets_menu",
)

@hooks.register("register_assets_menu")
def register_assets_menu():
    return register_images_menu_item()

@hooks.register("register_assets_menu")
def register_documents_menu():
    return register_documents_menu_item()

@hooks.register("register_assets_menu")
def register_collections_menu():
    return register_collections_menu_item()

@hooks.register("register_admin_menu_item")
def register_assets_submenu():
    return SubmenuMenuItem(
        _("Assets"),
        name="assets",
        icon_name="folder-open-1",
        menu=assets_menu,
        classnames="sidebar-menu-item",
        order=300,
    )

@hooks.register("construct_settings_menu")
def hide_settings_items(request, menu_items):
    menu_items[:] = filter(lambda item: item.name not in HIDDEN_SETTINGS_MENU_ITEMS, menu_items)

@hooks.register("construct_main_menu")
def hide_main_items(request, menu_items):
    menu_items[:] = filter(lambda item: item.name not in HIDDEN_MAIN_MENU_ITEMS, menu_items)
