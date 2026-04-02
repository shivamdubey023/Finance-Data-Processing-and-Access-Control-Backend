import graphene 
from graphene_django import DjangoObjectType
from .models import User, Category, FinancialRecod


# Settings for GraphQL schema and types 

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')

class FinancialRecodType(DjangoObjectType):
    class Meta:
        model = FinancialRecod
        fields = ('id', 'amount', 'type', 'Category', 'created_by', 'owner', 'date', 'notes')


# Define the GraphQL schema

class Query(graphene.ObjectType):
    all_financial_records = graphene.List(FinancialRecodType)

    def resolve_all_financial_records(root, info):
        return FinancialRecod.objects.all()
    




    