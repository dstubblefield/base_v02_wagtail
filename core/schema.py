# File: core/schema.py

import graphene
import landing_funnels.schema  # Import landing_funnels schema
import blog.schema  # Import blog schema
import faq.schema  # Import faq schema
import flex.schema  # Import flex schema
import home.schema  # Import home schema
import location_funnels.schema  # Import location_funnels schema
import products.schema  # Import products schema
import services.schema  # Import services schema

class Query(
    landing_funnels.schema.Query,
    blog.schema.Query,
    faq.schema.Query,
    flex.schema.Query,
    home.schema.Query,
    location_funnels.schema.Query,
    products.schema.Query,
    services.schema.Query,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)

