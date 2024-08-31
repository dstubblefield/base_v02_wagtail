# blog/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from wagtail.rich_text import RichText
from .models import BlogDetail, BlogIndex
from taggit.models import Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ['name']


class BlogDetailType(DjangoObjectType):
    tags = graphene.List(TagType)
    body = graphene.String()

    class Meta:
        model = BlogDetail
        exclude = ['tags', 'body']

    def resolve_tags(self, info):
        return self.tags.all()

    def resolve_body(self, info):
        return self.body.stream_data if self.body else ""


class BlogIndexType(DjangoObjectType):
    class Meta:
        model = BlogIndex
        fields = '__all__'


class Query(graphene.ObjectType):
    blog_detail = graphene.Field(BlogDetailType, id=graphene.Int())
    all_blog_details = graphene.List(BlogDetailType)

    blog_index = graphene.Field(BlogIndexType, id=graphene.Int())
    all_blog_indices = graphene.List(BlogIndexType)

    def resolve_blog_detail(self, info, id):
        return BlogDetail.objects.get(pk=id)

    def resolve_all_blog_details(self, info):
        return BlogDetail.objects.all()

    def resolve_blog_index(self, info, id):
        return BlogIndex.objects.get(pk=id)

    def resolve_all_blog_indices(self, info):
        return BlogIndex.objects.all()
