from django.db import models
from wagtail.images import get_image_model
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.fields import RichTextField
from app_blocks import blocks as custom_blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, FieldRowPanel, HelpPanel, MultipleChooserPanel, TitleFieldPanel


class FaqPage(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    child_page_types = []
    
    
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    
    hero_image_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 1920-w x 1200-h pixels.",
        related_name='+'
    )
    hero_image_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait 800-w x12000-h pixels.",
        related_name='+'
    )
    
    about = RichTextField(blank=True, null=True, features=['bold', 'italic', 'link'])
    
    
    body = StreamField([
        ('faq', custom_blocks.FAQListBlock()),
    ])
    
    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        FieldPanel('hero_image_desktop'),
        FieldPanel('hero_image_mobile'),
        FieldPanel('about'),
        FieldPanel('body'),
    ]
    
    

