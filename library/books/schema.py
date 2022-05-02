import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    world = graphene.String(default_value="World!")

schema = graphene.Schema(query=Query)