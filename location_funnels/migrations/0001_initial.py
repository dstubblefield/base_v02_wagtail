# Generated by Django 5.1 on 2024-08-29 13:31

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.fields
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
    ]

    operations = [
        migrations.CreateModel(
            name="LocationIndexPage",
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
                ("sub_title", models.CharField(blank=True, max_length=255, null=True)),
                ("body", wagtail.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Serviced Area Index Page",
                "verbose_name_plural": "Serviced Areas Index Pages",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LocationPageArea",
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
                ("sub_title", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Service Area (County or City)",
                "verbose_name_plural": "Service Areas (Counties or Cities)",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LocationPage",
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
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "state",
                    models.CharField(
                        blank=True, default="Illinois", max_length=100, null=True
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [("rich_text", 1), ("hero_block", 9)],
                        blank=True,
                        block_lookup={
                            0: (
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
                            1: ("wagtail.blocks.StructBlock", [[("content", 0)]], {}),
                            2: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "Image needs to be landscape 1920-w x 1200-h pixels."
                                },
                            ),
                            3: (
                                "wagtail.images.blocks.ImageChooserBlock",
                                (),
                                {
                                    "help_text": "Image needs to be portrait 800-w x 1200-h pixels."
                                },
                            ),
                            4: (
                                "wagtail.blocks.CharBlock",
                                (),
                                {
                                    "blank": True,
                                    "help_text": "Optional",
                                    "required": False,
                                },
                            ),
                            5: (
                                "wagtail.blocks.TextBlock",
                                (),
                                {
                                    "blank": True,
                                    "help_text": "Optional",
                                    "required": False,
                                },
                            ),
                            6: ("wagtail.blocks.CharBlock", (), {}),
                            7: (
                                "wagtail.blocks.PageChooserBlock",
                                (),
                                {"required": False},
                            ),
                            8: (
                                "wagtail.blocks.StructBlock",
                                [
                                    [
                                        ("image_desktop", 2),
                                        ("image_mobile", 3),
                                        ("title", 4),
                                        ("text", 5),
                                        ("button", 6),
                                        ("page_chooser", 7),
                                    ]
                                ],
                                {},
                            ),
                            9: ("wagtail.blocks.StreamBlock", [[("hero", 8)]], {}),
                        },
                        null=True,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app_snippets.author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Service Area Detail Page",
                "verbose_name_plural": "Service Area Detail Pages",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LocationPageTags",
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
                        to="location_funnels.locationpage",
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
            model_name="locationpage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="location_funnels.LocationPageTags",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
