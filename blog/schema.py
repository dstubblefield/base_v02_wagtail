# File: blog/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from .models import BlogDetail, BlogIndex
from taggit.models import Tag

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class BlogDetailType(DjangoObjectType):
    tags = graphene.List(TagType)
    body = graphene.String()

    class Meta:
        model = BlogDetail
        exclude = ('tags', 'body')  # Exclude tags and body from auto conversion

    def resolve_tags(self, info):
        return self.tags.all()

    def resolve_body(self, info):
        return str(self.body)  # Simplified resolver for StreamField

class BlogIndexType(DjangoObjectType):
    class Meta:
        model = BlogIndex

class Query(graphene.ObjectType):
    blog_post = graphene.Field(BlogDetailType, id=graphene.Int())
    all_blog_posts = graphene.List(BlogDetailType)

    blog_index = graphene.Field(BlogIndexType, id=graphene.Int())
    all_blog_indexes = graphene.List(BlogIndexType)

    def resolve_blog_post(self, info, id):
        return BlogDetail.objects.get(pk=id)

    def resolve_all_blog_posts(self, info):
        return BlogDetail.objects.all()

    def resolve_blog_index(self, info, id):
        return BlogIndex.objects.get(pk=id)

    def resolve_all_blog_indexes(self, info):
        return BlogIndex.objects.all()
