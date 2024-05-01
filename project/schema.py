import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id','username','email')






# api views 
class Query(graphene.ObjectType):
    user = graphene.List(
        UserType,
    )
    def resolve_authors(self,info,search=None,order=None):
        query = User.objects.all() 
        return query

schema = graphene.Schema(query=Query)