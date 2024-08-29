#staff/models.py
from django.db import models

from django import forms
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images import get_image_model
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from app_blocks.blocks import ExternalLinkBlock
from app_forms.forms import GenericStaffForm


class StaffIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['staff.StaffPage']  # Restrict child page types
    # Add any specific fields for the category if needed
    template = "staff/staff_index_page.html"
    
    staff_hero = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    staff_hero_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    
    def get_context(self, request):
        context = super().get_context(request)
        context['staffpage'] = StaffPage.objects.live().public()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('staff_hero'),
        FieldPanel('staff_hero_mobile'),
        FieldPanel('subtitle'),
        FieldPanel('description'),
    ]
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        

class StaffPage(Page):
    base_form_class = GenericStaffForm
    parent_page_types = ['staff.StaffIndex']
    sub_page_types = []
    template = "staff/staff_page.html"
    
    ROLE_CHOICES = (
        ('owner', 'Owner / CEO'),
        ('office', 'Office Staff'),
        ('sales', 'Sales'),
        ('project_manager', 'Project Manager'),
    )
    
    job_title = models.CharField(max_length=255, blank=True)
    job_catagory = models.CharField(
        max_length=255, choices=ROLE_CHOICES)
    email = models.EmailField( blank=True, null=True)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    office_phone_ext = models.CharField(max_length=10, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    
    bio = RichTextField(blank=True)
    headshot = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    social_media_links = StreamField([
        ('social_media_link', ExternalLinkBlock())
    ], use_json_field=True, blank=True, null=True)
    
    counties = models.ManyToManyField('admin_snippets.County', blank=True)
    
    
    content_panels = Page.content_panels + [
        FieldPanel('job_title'),
        FieldPanel('job_catagory'),
        MultiFieldPanel(
            [
            FieldPanel('email'),
        FieldRowPanel(
            [
            FieldPanel('office_phone'),
            FieldPanel('office_phone_ext'),
        ]
            ),
        FieldPanel('mobile_phone'),
            ], heading="Contact Information"
        ),
        MultiFieldPanel(
            [
            FieldPanel('bio'),
            FieldPanel('headshot'),
        ], heading="Bio and Headshot"
        ),
        FieldPanel('social_media_links'),
        FieldPanel('counties', widget=forms.CheckboxSelectMultiple),
    ]
    
    