from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultipleChooserPanel
from wagtail.documents import get_document_model
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.images import get_image_model

class ProductsIndex(Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['products.ProductsCategoryPage']  # Restrict child page types
    # Add any specific fields for the category if needed
    category_hero_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be 1920 pixels wide and 1200 pixels high.",
        related_name='+',
    )
    category_hero_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be 800 pixels wide and 1200 pixels high.",
        related_name='+',
    )
    description = RichTextField(blank=True)
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['categories'] = ProductsCategoryPage.objects.live().public()
        return context
        

    content_panels = Page.content_panels + [
        FieldPanel('category_hero_desktop'),
        FieldPanel('category_hero_mobile'),
        FieldPanel('description'),
    ]

    
    
    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
        
class ProductPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'products.ProductPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
        )

class ProductsCategoryPage(Page):
    # Fields specific to the subcategory
    subcategory_hero_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 1920-w x1080-h pixels.",
        related_name='+'
    )
    subcategory_hero_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait 800-w x1200-h pixels.",
        related_name='+'
    )
    menu_title = models.CharField(max_length=100, blank=True)
    category_brochure = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    details = RichTextField(blank=True)
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['products'] = ProductPage.objects.child_of(self).live().public()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('menu_title'),
        FieldPanel('subcategory_hero_desktop'),
        FieldPanel('subcategory_hero_mobile'),
        FieldPanel('category_brochure'),
        FieldPanel('details'),
    ]

    parent_page_types = ['products.ProductsIndex']  # Restrict parent page type
    subpage_types = ['products.ProductPage']  # Restrict child page types
    
    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Products Categories"

class ProductPage(Page):
    # Product specific fields
    menu_title = models.CharField(max_length=100, blank=True)
    product_hero_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 1920-w x1080-h pixels.",
        related_name='+'
    )
    product_hero_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portraits 800-w x 1,200-h pixels.",
        related_name='+'
    )
    tags = ClusterTaggableManager(through=ProductPageTags, blank=True)
    brochure = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('menu_title'),
        FieldPanel('product_hero_desktop'),
        FieldPanel('product_hero_mobile'),
        FieldPanel("tags"),
        MultipleChooserPanel('gallery_images', label="Gallery images", chooser_field_name="image"),
        FieldPanel('brochure'),
        FieldPanel('description'),
    ]

    parent_page_types = ['products.ProductsCategoryPage']  # Restrict parent page type
    child_page_types = []  # No child pages allowed
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
class ProductPageGalleryImage(Orderable):
    page = ParentalKey(ProductPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True,
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]