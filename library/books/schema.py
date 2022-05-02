import graphene
from graphene_django import DjangoObjectType
from library.books.models import *

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name',)

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'

class BookQuery(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    book_by_name = graphene.Field(BookType, name=graphene.String(required=True))
	#books_by_author_id = graphene.List(AuthorsType, author_id=graphene.Int(required=True))

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_book_by_name(root, info, name):
        try:
            return Book.objects.get(name=name)
        except Book.DoesNotExist:
            return None

class Query(BookQuery, graphene.ObjectType):
    pass
    # book_queries = BookQuery()

class AuthorMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        name = graphene.String(required=True)
        last_name = graphene.String()

    # The class attributes define the response of the mutation
    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id, name, last_name):
        author = Author.objects.get(pk=id)
        author.name = name
        author.last_name = last_name
        author.save()
        # Notice we return an instance of this mutation
        return AuthorMutation(author=author)

class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)