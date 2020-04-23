import graphene

from links.schema import LinkQuery, LinkMutation


class Query(LinkQuery, graphene.ObjectType):
  pass

class Mutation(LinkMutation, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
