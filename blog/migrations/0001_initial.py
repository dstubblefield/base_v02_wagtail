# Generated by Django 5.1 on 2024-08-30 17:42

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.contrib.routable_page.models
import wagtail.fields
import wagtailmarkdown.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_snippets", "0001_initial"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogDetail",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("subtitle", models.CharField(blank=True, max_length=255)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("faq", 0),
                            ("text", 1),
                            ("rich_text_block", 3),
                            ("banner", 6),
                            ("cta", 10),
                            ("markdown", 11),
                        ],
                        blank=True,
                        block_lookup={
                            0: ("app_blocks.blocks.FAQListBlock", (), {}),
                            1: ("app_blocks.blocks.TextBlock", (), {}),
                            2: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {
                                    "features": [
                                        "h2",
                                        "h3",
                                        "bold",
                                        "italic",
                                        "ol",
                                        "ul",
                                        "link",
                                        "blockquote",
                                    ]
                                },
                            ),
                            3: ("wagtail.blocks.StructBlock", [[("content", 2)]], {}),
                            4: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {"required": True},
                            ),
                            5: ("wagtail.blocks.CharBlock", (), {"required": False}),
                            6: (
                                "wagtail.blocks.StructBlock",
                                [[("image", 4), ("caption", 5)]],
                                {},
                            ),
                            7: (
                                "wagtail.blocks.RichTextBlock",
                                (),
                                {"features": ["bold", "italic"]},
                            ),
                            8: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "help_text": "Button text",
                                    "max_length": 100,
                                    "required": True,
                                },
                            ),
                            9: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": True},
                            ),
                            10: (
                                "wagtail.blocks.StructBlock",
                                [[("text", 7), ("button", 8), ("page_chooser", 9)]],
                                {},
                            ),
                            11: ("wagtailmarkdown.blocks.MarkdownBlock", (), {}),
                        },
                        null=True,
                        verbose_name="Body Content",
                    ),
                ),
                (
                    "markdown_field",
                    wagtailmarkdown.fields.MarkdownField(
                        blank=True, null=True, verbose_name="Markdown Field"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="app_snippets.author",
                    ),
                ),
                (
                    "hero_image_desktop",
                    models.ForeignKey(
                        blank=True,
                        help_text="Image needs to be landscape 1920-w x1200-h pixels.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "hero_image_mobile",
                    models.ForeignKey(
                        blank=True,
                        help_text="Image needs to be portrait 800-w x1200-h pixels.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.CreateModel(
            name="BlogIndex",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("subtitle", models.CharField(blank=True, max_length=100)),
                (
                    "body",
                    wagtail.fields.RichTextField(
                        blank=True,
                        help_text="This text will appear on the blog landing page",
                    ),
                ),
                (
                    "hero_image_desktop",
                    models.ForeignKey(
                        blank=True,
                        help_text="Image needs to be landscape 1920-w x 1200-h pixels.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "hero_image_mobile",
                    models.ForeignKey(
                        blank=True,
                        help_text="Image needs to be portrait 800-w x12000-h pixels.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog Landing Page",
                "verbose_name_plural": "Blog Landing Pages",
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.CreateModel(
            name="BlogPageTags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="blog.blogdetail",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="blogdetail",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.BlogPageTags",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
