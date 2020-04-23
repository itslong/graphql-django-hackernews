import graphene

from links.schema import LinkQuery


class Query(LinkQuery, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)
