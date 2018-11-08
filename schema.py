import graphene


class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

    
class Query(graphene.ObjectType):
  hello = graphene.String(name=graphene.String(default_value="World"))

  def resolve_hello(self, info, name):
    return 'Hello ' + name

schema = graphene.Schema(query=Query)
