from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from app_blocks import blocks as custom_blocks
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    max_count = 1
    template = "home/home_page.html"
    
    body = StreamField([
        ('rich_text', custom_blocks.RichTextBlock()),
        ('hero', custom_blocks.HeroBlock()), 
    ],
        block_counts={},
        use_json_field=True, 
        blank=True,
        null=True
        )
    content_panels = Page.content_panels + [
        
        FieldPanel('body'),
    ]
                       
