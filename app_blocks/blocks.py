# app_blocks/blocks.py

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from django.core.exceptions import ValidationError

class AddressBlock(blocks.StructBlock):
    street = blocks.CharBlock()
    city = blocks.CharBlock()
    state = blocks.CharBlock()
    zip_code = blocks.CharBlock(default="Illinois")

    class Meta:
        icon = "site"
        template = "app_blocks/address_block.html"
        label = "Address"
        group = "Address"
        admin_text = "Add an address"


class CountyBlock(blocks.CharBlock):

    class Meta:
        icon = "site"
        template = "app_blocks/county_block.html"
        label = "County"
        group = "Address"
        admin_text = "Add a county"


class ExternalLinkBlock(blocks.StructBlock):
    link_title = blocks.CharBlock(max_length=100, label="External Link Title")
    link_block_external = blocks.URLBlock(required=False, label="External Link URL. Use https://www.example.com")

    class Meta:
        icon = "link"
        template = "app_blocks/external_link_block.html"
        label = "External Link"
        group = "Links"
        admin_text = "Add an external link to a website, social media, company page, or other external page"


class CarouselBlock(blocks.StreamBlock):
    slide = blocks.StructBlock([
        ('image_desktop', ImageChooserBlock(help_text="Image needs to be landscape 1920-w x 1200-h pixels.")),
        ('title', blocks.CharBlock()),
        ('text', blocks.TextBlock()),
        ('button', blocks.CharBlock()),
        ('page_chooser', blocks.PageChooserBlock(required=False)),
    ])

    def clean(self, value):
        value = super().clean(value)
        if len(value) < 2:
            raise ValidationError("You must have at least two slides.")
        return value

    class Meta:
        icon = "cog"
        template = "app_blocks/carousel_block.html"
        label = "Carousel"
        group = "Hero"
        admin_text = "Add a slide to the hero carousel, with title, text, and button"


class HeroBlock(blocks.StreamBlock):
    hero = blocks.StructBlock([
        ('image_desktop', ImageChooserBlock(
            help_text="Image needs to be landscape 1920-w x 1200-h pixels."
        )),
        ('image_mobile', ImageChooserBlock(
            help_text="Image needs to be portrait 800-w x 1200-h pixels."
        )),
        ('title', blocks.CharBlock(required=False, help_text="Optional")),
        ('text', blocks.TextBlock(required=False, help_text="Optional")),
        ('button', blocks.CharBlock()),
        ('page_chooser', blocks.PageChooserBlock(required=False)),
    ])

    class Meta:
        icon = "image"
        template = "app_blocks/hero_block.html"
        label = "Hero"
        group = "Hero"
        admin_text = "Add a hero image with title, text, and button"


class VideoBlock(blocks.StructBlock):
    video = EmbedBlock()

    class Meta:
        icon = "cog"
        template = "app_blocks/video_block.html"
        label = "Video"
        group = "Hero"


class ImageGalleryBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock())
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "app_blocks/image_gallery_block.html"
        label = "Image Gallery"
        group = "Images"
        admin_text = "Add an image gallery"


class ImageBannerBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "app_blocks/image_banner_block.html"
        label = "Image Banner"
        group = "Images"
        admin_text = "Add an image"


class H2Block(blocks.TextBlock):
    text = blocks.CharBlock()

    class Meta:
        icon = "title"
        template = "app_blocks/h2_block.html"
        label = "Heading 2"
        group = "Text"
        admin_text = "Add an H2 heading"


class H3Block(blocks.TextBlock):

    class Meta:
        icon = "title"
        template = "app_blocks/h3_block.html"
        label = "Heading 3"
        group = "Text"
        admin_text = "Add an H3 heading"


class TextBlock(blocks.TextBlock):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, help_text="Add a simple text block, min 10 characters.", min_length=10, required=False)

    def clean(self, value):
        value = super().clean(value)
        if value.strip() == "":
            raise ValidationError("This field cannot be empty.")
        return value

    class Meta:
        icon = "doc-empty"
        template = "app_blocks/text_block.html"
        label = "Text"
        group = "Text"
        admin_text = "Add a simple text block"


class MarkDownBlock(blocks.StreamBlock):
    markdown = MarkdownBlock()

    class Meta:
        icon = "doc-full"
        template = "app_blocks/markdown_block.html"
        label = "Markdown"
        group = "Text"
        admin_text = "Add a markdown code block"


class AuthorBlock(blocks.StructBlock):
    author = SnippetChooserBlock('blog.Author')

    class Meta:
        icon = "user"
        template = "app_blocks/author_block.html"
        label = "Author"
        group = "Text"
        admin_text = "Add an author"


class RichTextBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'ol', 'ul', 'link', 'blockquote'])

    class Meta:
        icon = "doc-full"
        template = "app_blocks/rich_text_block.html"
        label = "Rich Text"
        group = "Text"
        admin_text = "Add a rich text block with headings, bold, italic, lists, blockquote, and links"


class QuoteBlock(blocks.TextBlock):

    class Meta:
        icon = "openquote"
        template = "app_blocks/quote_block.html"
        label = "Quote"
        group = "Text"
        admin_text = "Add a quote"


class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock()
    answer = blocks.RichTextBlock(features=['bold', 'italic'])


class FAQListBlock(blocks.ListBlock):
    def __init__(self, **kwargs):
        super().__init__(FAQBlock(), **kwargs)

    class Meta:
        icon = "help"
        template = "app_blocks/faq_block.html"
        label = "Frequently Asked Questions"
        group = "Text"
        admin_text = "Add a list of frequently asked questions"


class CallToActionBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(features=['bold', 'italic'])
    button = blocks.CharBlock(max_length=100, required=True, help_text="Button text")
    page_chooser = blocks.PageChooserBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        page = value.get('page_chooser')
        button = value.get('button')
        context['button_text'] = button if button else f'Read more about {page.title}'
        return context

    class Meta:
        icon = "cog"
        template = "app_blocks/call_to_action_block.html"
        label = "Call to Action"
        group = "Text"
        admin_text = "Add a call to action with title, text, and button"
