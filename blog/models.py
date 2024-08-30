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
from app_snippets.models import Author

class BlogPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'blog.BlogDetail',
        related_name='tagged_items',
        on_delete=models.CASCADE,
        )

class BlogIndex(RoutablePageMixin, Page):
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogDetail']
    template = "blog/blog_index_page.html"
    
    subtitle = models.CharField(max_length=100, blank=True)
    
    body = RichTextField(
        blank=True, 
        help_text="This text will appear on the blog landing page",
        features=['h2', 'h3', 'bold', 'italic', 'strikethrough', 'link', 'ol', 'ul', 'blockquote']
        )
    
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

    content_panels = Page.content_panels + [
        FieldPanel('hero_image_desktop'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        
    ]
    
    @path('all/', name='all')
    def all_blog_posts(self, request):
        post = BlogDetail.objects.live().public().order_by('-first_published_at')
        
        return self.render(
            request,
            context_overrides={
                'post': post,
                
            }
            
        )

    @path('tags/<str:tag>/', name='tags')
    def blog_posts_by_tag(self, request, tag=None):
        posts = BlogDetail.objects.live().public().filter(tags__name=tag)
        
        return self.render(
            request,
            context_overrides={
                'posts': posts,
                'tag': tag,
            }, template='blog/blog_tag_page.html'
        )
        
    
    
    
        
    def get_context(self, request):
        context = super().get_context(request)
        context['blogpages'] = BlogDetail.objects.live().public().order_by('-first_published_at')[:5]
        return context
    
    class Meta:
        verbose_name = "Blog Landing Page"
        verbose_name_plural = "Blog Landing Pages"



class BlogDetail(RoutablePageMixin, Page):
    parent_page_types = ['blog.BlogIndex']
    subpage_types = []
    template = "blog/blog_detail.html"
    
    hero_image_desktop = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be landscape 1920-w x1200-h pixels.",
        related_name='+'
    )
    
    hero_image_mobile = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Image needs to be portrait 800-w x1200-h pixels.",
        related_name='+'
    )
    
    author = models.ForeignKey(
        'app_snippets.Author',  # Use your actual app name here
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',  # Prevents reverse relation
    )

    subtitle = models.CharField(max_length=255, blank=True)
    

    body = StreamField([
        ('faq', custom_blocks.FAQListBlock()),
        ('text', custom_blocks.TextBlock()),
        ('rich_text_block', custom_blocks.RichTextBlock()),
        ('banner', custom_blocks.ImageBannerBlock()),
        ('cta', custom_blocks.CallToActionBlock()),
        ('markdown', custom_blocks.MarkdownBlock()),
    ], block_counts={
        # 'text': {'min_num': 1, 'max_num': 1},
        
    },
    use_json_field=True, 
    blank=True, 
    null=True, 
    verbose_name="Body Content"
    )
    markdown_field = MarkdownField(blank=True, null=True, verbose_name="Markdown Field")
    
    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)
    
    @path('all/', name='all')
    def all_blog_posts(self, request):
        post = BlogDetail.objects.live().public().order_by('-first_published_at')
        
        return self.render(
            request,
            context_overrides={
                'post': post,
                
            }
            
        )

    @path('tags/<str:tag>/', name='tags')
    def blog_posts_by_tag(self, request, tag=None):
        posts = BlogDetail.objects.live().public().filter(tags__name=tag)
        
        return self.render(
            request,
            context_overrides={
                'posts': posts,
                'tag': tag,
            }, template='blog/blog_tag_page.html'
        )


    content_panels = Page.content_panels + [
        
        FieldPanel('hero_image_desktop'),
        FieldPanel('hero_image_mobile'),
        FieldPanel('author'),
        FieldPanel('tags'),
        FieldPanel('subtitle'),
        
        FieldPanel('body'),
        FieldPanel('markdown_field'),  
        
    ]
    
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
    def clean(self):
        super().clean()
        
        errors = {}
        
        if 'blog' in self.title.lower():
            errors['title'] = ValidationError("The word 'Blog' in the title is not allowed")
            
        if 'blog' in self.subtitle.lower():
            errors['subtitle'] = ValidationError("The word 'Blog' in the subtitle is not allowed")
            
        if 'blog' in self.slug.lower():
            errors['slug'] = ValidationError("The word 'Blog' in the slug is not allowed")
        
        if 'post' in self.title.lower():
            errors['title'] = ValidationError("The word 'Post' in the title is not allowed")
            
        if 'post' in self.subtitle.lower():
            errors['subtitle'] = ValidationError("The word 'Post' in the subtitle is not allowed")
            
        if 'post' in self.slug.lower():
            errors['slug'] = ValidationError("The word 'Post' in the slug is not allowed")
        
        
        if errors:
            raise ValidationError(errors)
