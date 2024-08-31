import graphene
from graphene_django.types import DjangoObjectType
from .models import LocationIndexPage, LocationPageArea, LocationPage
from graphene import relay

class LocationPageType(DjangoObjectType):
    body = graphene.String()
    tags = graphene.List(graphene.String)

    class Meta:
        model = LocationPage
        exclude = ['body', 'tags']

    def resolve_body(self, info):
        return self.body.stream_data if self.body else ""

    def resolve_tags(self, info):
        return [tag.name for tag in self.tags.all()]

class LocationPageAreaType(DjangoObjectType):
    class Meta:
        model = LocationPageArea

class LocationIndexPageType(DjangoObjectType):
    class Meta:
        model = LocationIndexPage

class Query(graphene.ObjectType):
    location_page = graphene.Field(LocationPageType, id=graphene.Int())
    location_page_area = graphene.Field(LocationPageAreaType, id=graphene.Int())
    location_index_page = graphene.Field(LocationIndexPageType, id=graphene.Int())

    def resolve_location_page(self, info, id):
        return LocationPage.objects.get(pk=id)

    def resolve_location_page_area(self, info, id):
        return LocationPageArea.objects.get(pk=id)

    def resolve_location_index_page(self, info, id):
        return LocationIndexPage.objects.get(pk=id)

schema = graphene.Schema(query=Query)
