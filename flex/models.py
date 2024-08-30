#flex/models.py
from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from app_blocks import blocks as custom_blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model

class FlexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []
    template = 'flex/flex_page.html'
    
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
    
    body = StreamField([
        ('rich_text', custom_blocks.RichTextBlock()),
        ('h2', custom_blocks.H2Block()),
        ('h3', custom_blocks.H3Block()),
        ('faq', custom_blocks.FAQListBlock()),
        ('cta', custom_blocks.CallToActionBlock()),
        ('quote', custom_blocks.QuoteBlock()),
        ('video', custom_blocks.VideoBlock()),
        ('image_gallery', custom_blocks.ImageGalleryBlock()),
        ('carousel', custom_blocks.CarouselBlock()),
        ('image_banner', custom_blocks.ImageBannerBlock())
        
    ],
        block_counts={},
        use_json_field=True, 
        blank=True,
        null=True
        )
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_image_desktop'),
        FieldPanel('hero_image_mobile'),
        FieldPanel('body')
        
    ]