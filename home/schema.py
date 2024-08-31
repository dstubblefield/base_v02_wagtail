import graphene
from graphene_django.types import DjangoObjectType
from .models import HomePage

class HomePageType(DjangoObjectType):
    body = graphene.String()

    class Meta:
        model = HomePage
        exclude = ['body']

    def resolve_body(self, info):
        return self.body.stream_data if self.body else ""

class Query(graphene.ObjectType):
    home_page = graphene.Field(HomePageType, id=graphene.Int())

    def resolve_home_page(self, info, id):
        return HomePage.objects.get(pk=id)

schema = graphene.Schema(query=Query)
