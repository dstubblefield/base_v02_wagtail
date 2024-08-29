from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from app_blocks import blocks as custom_blocks
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.fields import RichTextField
from home.models import HomePage
from app_snippets.models import Author
from django.utils.translation import gettext_lazy as _
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet
# from .panels import SubcategoryChooser

class LandingPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'landing_funnels.LandingPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
        )
    
class LandingIndexPage(Page):
    max_count = 1
    parent_type = ['home.HomePage']
    subpage_types = ['landing_funnels.LandingPageArea']
    template = 'landing_funnels/landing_index_page.html'
    
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        landing_pages_area = LandingPage.objects.live().public()
        context['landing_pages_area'] = landing_pages_area
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        FieldPanel('body'),
    ]
    class Meta:
        verbose_name = "Landing Pages Index Page"
        verbose_name_plural = "Landing Pages Index Pages"
        
class LandingPageArea(Page):
        parent_page_types = ['landing_funnels.LandingIndexPage']
        subpage_types = ['landing_funnels.LandingPage']
        template = 'landing_funnels/landing_index_page.html'
        
        sub_title = models.CharField(max_length=255, blank=True, null=True)
        
        def get_context(self, request, *args, **kwargs):
            context = super().get_context(request, *args, **kwargs)
            landing_funnels = LandingPage.objects.live().public()
            context['landing_pages'] = landing_pages
            return context
        
        content_panels = Page.content_panels + [
            FieldPanel('sub_title'),
        ]
        
        class Meta:
            verbose_name = "Service Area (County or City)"
            verbose_name_plural = "Service Areas (Counties or Cities)"
        

class LandingPage(Page):
    parent_page_types = ['landing_funnels.LandingPageArea']
    subpage_types = []
    template = 'landing_funnels/landing_page.html'
    
    tags = ClusterTaggableManager(through=LandingPageTags, blank=True)
    
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    # county = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True, default="Illinois")
    
    body = StreamField([
        ('rich_text', custom_blocks.RichTextBlock()),
        ('hero_block', custom_blocks.HeroBlock()),  
        
    ],
        block_counts={},
        use_json_field=True, 
        blank=True,
        null=True
        )
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        home_page = HomePage.objects.first()
        if home_page:
            hero_html_content = []
            for block in home_page.body:
                if block.block_type == 'hero':
                    hero_html_content.append(block)  # Append the block     itself, which renders as HTML
            context['home_hero_html_content'] = hero_html_content
        return context
        
    content_panels = Page.content_panels + [
        FieldPanel('author'), 
        FieldPanel('tags'),
        # FieldPanel('county'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('body'),
    ]
    
    class Meta:
        verbose_name = "Service Area Detail Page"
        verbose_name_plural = "Service Area Detail Pages"
      
                       
