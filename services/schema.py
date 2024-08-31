import graphene
from graphene_django.types import DjangoObjectType
from .models import ServicesIndex, ServicesCategoryPage, ServicePage

class ServicePageType(DjangoObjectType):
    tags = graphene.List(graphene.String)

    class Meta:
        model = ServicePage
        exclude = ['tags']

    def resolve_tags(self, info):
        return [tag.name for tag in self.tags.all()]

class ServicesCategoryPageType(DjangoObjectType):
    class Meta:
        model = ServicesCategoryPage

class ServicesIndexType(DjangoObjectType):
    class Meta:
        model = ServicesIndex

class Query(graphene.ObjectType):
    service_page = graphene.Field(ServicePageType, id=graphene.Int())
    services_category_page = graphene.Field(ServicesCategoryPageType, id=graphene.Int())
    services_index = graphene.Field(ServicesIndexType, id=graphene.Int())

    def resolve_service_page(self, info, id):
        return ServicePage.objects.get(pk=id)

    def resolve_services_category_page(self, info, id):
        return ServicesCategoryPage.objects.get(pk=id)

    def resolve_services_index(self, info, id):
        return ServicesIndex.objects.get(pk=id)

schema = graphene.Schema(query=Query)
