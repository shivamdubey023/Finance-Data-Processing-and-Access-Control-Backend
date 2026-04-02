import graphene
from graphene_django import DjangoObjectType
from finance.schema import Query as FinanceQuery


class Query(FinanceQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

