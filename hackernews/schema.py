import graphene
import graphql_jwt

from links.schema import LinkQuery, LinkMutation
from users.schema import UserMutation, UserQuery


class Query(LinkQuery, UserQuery, graphene.ObjectType):
  pass

class Mutation(LinkMutation, UserMutation, graphene.ObjectType):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
