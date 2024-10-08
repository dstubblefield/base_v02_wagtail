# Generated by Django 5.1 on 2024-08-30 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_blogdetail_options"),
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetail",
            name="hero_image_desktop",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be landscape 1920-w x1200-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AlterField(
            model_name="blogdetail",
            name="hero_image_mobile",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be portrait 800-w x1200-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AlterField(
            model_name="blogindex",
            name="hero_image_desktop",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be landscape 1920-w x 1200-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AlterField(
            model_name="blogindex",
            name="hero_image_mobile",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be portrait 800-w x12000-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
    ]
