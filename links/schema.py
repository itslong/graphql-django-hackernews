import graphene
from graphene_django import DjangoObjectType

from .models import Link


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
    link = Link(url=url, description=description)
    link.save()

    return CreateLink(
      id=link.id,
      url=link.url,
      description=link.description,
    )


class LinkMutation(graphene.ObjectType):
  """
  Field to be resolved.
  """
  create_link = CreateLink.Field()
