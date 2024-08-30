# File: landing_funnels/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from .models import LandingPage, LandingPageArea, LandingIndexPage
from taggit.models import Tag

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class LandingPageType(DjangoObjectType):
    tags = graphene.List(TagType)
    body = graphene.String()

    class Meta:
        model = LandingPage
        exclude = ('tags', 'body')  # Exclude tags and body from auto conversion

    def resolve_tags(self, info):
        return self.tags.all()

    def resolve_body(self, info):
        return str(self.body)  # Simplified resolver for StreamField

class LandingPageAreaType(DjangoObjectType):
    class Meta:
        model = LandingPageArea

class LandingIndexPageType(DjangoObjectType):
    class Meta:
        model = LandingIndexPage

class Query(graphene.ObjectType):
    landing_page = graphene.Field(LandingPageType, id=graphene.Int())
    all_landing_pages = graphene.List(LandingPageType)

    landing_page_area = graphene.Field(LandingPageAreaType, id=graphene.Int())
    all_landing_page_areas = graphene.List(LandingPageAreaType)

    landing_index_page = graphene.Field(LandingIndexPageType, id=graphene.Int())
    all_landing_index_pages = graphene.List(LandingIndexPageType)

    def resolve_landing_page(self, info, id):
        return LandingPage.objects.get(pk=id)

    def resolve_all_landing_pages(self, info):
        return LandingPage.objects.all()

    def resolve_landing_page_area(self, info, id):
        return LandingPageArea.objects.get(pk=id)

    def resolve_all_landing_page_areas(self, info):
        return LandingPageArea.objects.all()

    def resolve_landing_index_page(self, info, id):
        return LandingIndexPage.objects.get(pk=id)

    def resolve_all_landing_index_pages(self, info):
        return LandingIndexPage.objects.all()
