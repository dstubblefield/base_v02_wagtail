# admin_snippets/models.py
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model
from django.core.exceptions import ValidationError
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.fields import StreamField
from wagtail.blocks import TextBlock, StreamBlock, StructBlock, CharBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from app_blocks import blocks as custom_blocks
from django.contrib.contenttypes.fields import GenericRelation
from wagtail.admin.panels import PublishingPanel
from wagtail.models import DraftStateMixin, RevisionMixin, LockableMixin, PreviewableMixin
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.search import index
from wagtailmarkdown.fields import MarkdownField

from wagtail.snippets.models import register_snippet


class Author(
    DraftStateMixin, 
    RevisionMixin, 
    LockableMixin,
    index.Indexed, 
    PreviewableMixin,
    models.Model):
    
    template = "blog/author.html"
    name = models.CharField(max_length=100)
    image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait",
        related_name='+'
    )
    title = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True, null=True)
    is_contributor = models.BooleanField(default=False)
    link = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    revisions = GenericRelation('wagtailcore.Revision', related_query_name='author')
    

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
        FieldPanel("title"),
        FieldPanel("bio"),
        FieldPanel("is_contributor"),
        FieldPanel("link"),
        PublishingPanel(),
        
    ]
    
    search_fields = [
        index.FilterField('name'),
        index.SearchField('bio'),
        index.AutocompleteField('name'),
    ]

    def __str__(self):
        return self.name
    
    @property
    def preview_modes(self):
        return PreviewableMixin.DEFAULT_PREVIEW_MODES + [
            ('dark_mode', 'Dark Mode')
        ]
    
    def get_preview_template(self, request, mode_name):
        templates = {
            "": "includes/author.html",
            "dark_mode": "includes/author_dark_mode.html",
        }
        return templates.get(mode_name,templates[""])
    

class County(models.Model):
    name = models.CharField(max_length=100)
    
    panels = [
        FieldPanel("name"),
        
    ]
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        related_name='cities'
    )
    state = models.CharField(max_length=20, default="Illinois")
    zip_code = models.CharField(max_length=10)
    description = RichTextField(blank=True)
    
    panels = [
        FieldPanel("name"),
        FieldPanel("county"),
        FieldPanel("state"),
        FieldPanel("zip_code"),
        FieldPanel("description"),
    ]
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']