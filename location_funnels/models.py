from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from app_blocks import blocks as custom_blocks
from home.models import HomePage
from app_snippets.models import Author

class LocationPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'location_funnels.LocationPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

class LocationIndexPage(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['location_funnels.LocationPageArea']
    template = 'location_funnels/landing_index_page.html'
    
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        location_pages_area = LocationPage.objects.live().public()
        context['location_pages_area'] = location_pages_area
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        FieldPanel('body'),
    ]
    
    class Meta:
        verbose_name = "Location Index Page"
        verbose_name_plural = "Location Index Pages"

class LocationPageArea(Page):
    parent_page_types = ['location_funnels.LocationIndexPage']
    subpage_types = ['location_funnels.LocationPage']
    template = 'location_funnels/location_index_page.html'
    
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        location_funnels = LocationPage.objects.live().public()
        context['location_funnels'] = location_funnels
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
    ]
    
    class Meta:
        verbose_name = "Location Area Page"
        verbose_name_plural = "Location Area Pages"

class LocationPage(Page):
    parent_page_types = ['location_funnels.LocationPageArea']
    subpage_types = []
    template = 'location_funnels/location_page.html'
    
    tags = ClusterTaggableManager(through=LocationPageTags, blank=True)
    
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
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
            hero_html_content = [block for block in home_page.body if block.block_type == 'hero']
            context['home_hero_html_content'] = hero_html_content
        return context
        
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('tags'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('body'),
    ]
    
    class Meta:
        verbose_name = "Location Detail Page"
        verbose_name_plural = "Location Detail Pages"
