import graphene
from jectman import schema
from graphene import relay, ObjectType


class Query(schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)