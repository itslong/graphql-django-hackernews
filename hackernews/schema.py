import graphene

from links.schema import LinkQuery, LinkMutation
from users.schema import UserMutation, UserQuery


class Query(LinkQuery, UserQuery, graphene.ObjectType):
  pass

class Mutation(LinkMutation, UserMutation, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
