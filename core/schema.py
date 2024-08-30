# File: core/schema.py

import graphene
import landing_funnels.schema  # Import landing_funnels schema
import blog.schema  # Import blog schema

class Query(landing_funnels.schema.Query, blog.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)