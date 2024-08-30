from django.db import models

# Create your models here.
from django.db import models

from wagtail.documents.models import AbstractDocument, Document


class CustomDocument(AbstractDocument):
    document_description = models.CharField(max_length=255, blank=True)
    admin_form_fields = Document.admin_form_fields + (
        'document_description',
    )
