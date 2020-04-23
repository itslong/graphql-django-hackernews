import graphene
from graphene_django import DjangoObjectType

from .models import Link, Vote
from users.schema import UserType


class LinkType(DjangoObjectType):
  class Meta:
    model = Link


class LinkQuery(graphene.ObjectType):
  links = graphene.List(LinkType)

  def resolve_links(self, info, **kwargs):
    return Link.objects.all()


class CreateLink(graphene.Mutation):
  """
  Defines a mutation class. Output can be defined field by field or just as a single field.
  Returns data back to the client.
  """
  id = graphene.Int()
  url = graphene.String()
  description = graphene.String()
  posted_by = graphene.Field(UserType)

  class Arguments:
    """
    Defines the data that can be sent to the server:
    url
    description
    """
    url = graphene.String()
    description = graphene.String()

  def mutate(self, info, url, description):
    """
    Creates a link in the db using the data sent by the user (url and description params).
    Returns a CreateLink class with the data just created. Must match the parameters defined at the top.
    """
    user = info.context.user or None

    link = Link(url=url, description=description, posted_by=user)
    link.save()

    return CreateLink(
      id=link.id,
      url=link.url,
      description=link.description,
      posted_by=link.posted_by
    )


class CreateVote(graphene.Mutation):
  user = graphene.Field(UserType)
  link = graphene.Field(LinkType)

  class Arguments:
    link_id = graphene.Int()

  def mutate(self, info, link_id):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('You must be logged in to vote')

    link = Link.objects.filter(id=link_id).first()
    if not link:
      raise Exception('Invalid Link')

    Vote.objects.create(
      user=user,
      link=link
    )

    return CreateVote(user=user, link=link)


class LinkMutation(graphene.ObjectType):
  """
  Field to be resolved.
  """
  create_link = CreateLink.Field()
  create_vote = CreateVote.Field()
