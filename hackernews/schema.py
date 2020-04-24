import graphene
import graphql_jwt

from links.schema import LinkQuery, LinkMutation
from users.schema import UserMutation, UserQuery
from links.schema_relay import RelayQuery, RelayMutation


class Query(LinkQuery, UserQuery, RelayQuery, graphene.ObjectType):
  pass

class Mutation(LinkMutation, UserMutation, RelayMutation, graphene.ObjectType):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
