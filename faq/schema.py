import graphene
from graphene_django.types import DjangoObjectType
from .models import FaqPage


class FaqPageType(DjangoObjectType):
    body = graphene.String()

    class Meta:
        model = FaqPage
        exclude = ['body']

    def resolve_body(self, info):
        return self.body.stream_data if self.body else ""


class Query(graphene.ObjectType):
    faq_page = graphene.Field(FaqPageType, id=graphene.Int())
    all_faq_pages = graphene.List(FaqPageType)

    def resolve_faq_page(self, info, id):
        return FaqPage.objects.get(pk=id)

    def resolve_all_faq_pages(self, info):
        return FaqPage.objects.all()
