import graphene
from graphene_django.types import DjangoObjectType
from .models import ProductsIndex, ProductsCategoryPage, ProductPage, ProductPageGalleryImage

class ProductPageGalleryImageType(DjangoObjectType):
    class Meta:
        model = ProductPageGalleryImage

class ProductPageType(DjangoObjectType):
    tags = graphene.List(graphene.String)
    gallery_images = graphene.List(ProductPageGalleryImageType)

    class Meta:
        model = ProductPage
        exclude = ['tags', 'gallery_images']

    def resolve_tags(self, info):
        return [tag.name for tag in self.tags.all()]

    def resolve_gallery_images(self, info):
        return self.gallery_images.all()

class ProductsCategoryPageType(DjangoObjectType):
    class Meta:
        model = ProductsCategoryPage

class ProductsIndexType(DjangoObjectType):
    class Meta:
        model = ProductsIndex

class Query(graphene.ObjectType):
    product_page = graphene.Field(ProductPageType, id=graphene.Int())
    products_category_page = graphene.Field(ProductsCategoryPageType, id=graphene.Int())
    products_index = graphene.Field(ProductsIndexType, id=graphene.Int())

    def resolve_product_page(self, info, id):
        return ProductPage.objects.get(pk=id)

    def resolve_products_category_page(self, info, id):
        return ProductsCategoryPage.objects.get(pk=id)

    def resolve_products_index(self, info, id):
        return ProductsIndex.objects.get(pk=id)

schema = graphene.Schema(query=Query)
