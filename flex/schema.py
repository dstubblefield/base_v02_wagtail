import graphene
from graphene_django.types import DjangoObjectType
from .models import FlexPage

class FlexPageType(DjangoObjectType):
    body = graphene.String()

    class Meta:
        model = FlexPage
        exclude = ['body']

    def resolve_body(self, info):
        return self.body.stream_data if self.body else ""

class Query(graphene.ObjectType):
    flex_page = graphene.Field(FlexPageType, id=graphene.Int())
    all_flex_pages = graphene.List(FlexPageType)

    def resolve_flex_page(self, info, id):
        return FlexPage.objects.get(pk=id)

    def resolve_all_flex_pages(self, info):
        return FlexPage.objects.all()

schema = graphene.Schema(query=Query)
