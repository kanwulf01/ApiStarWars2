import graphene
from graphene_django.types import DjangoObjectType
from movies.models import Personaje, Pelicula, Category2,Movie2,Category,Category1,Movie1, Movie, Producer, Character, Producer2, Planet, Character2, Film, Film2


class PersonajeType(DjangoObjectType):
  class Meta:
    model = Personaje

class PeliculaType(DjangoObjectType):
  class Meta:
    model = Pelicula
    fields = ('id','personaje_id',)

class CategoryType(DjangoObjectType):
  class Meta:
    model = Category

class Category1Type(DjangoObjectType):
  class Meta:
    model = Category1


class Category2Type(DjangoObjectType):
  class Meta:
    model = Category2

class Movie1Type(DjangoObjectType):

  class Meta:
    model = Movie1

class Movie2Type(DjangoObjectType):

  class Meta:
    model = Movie2

class MovieType(DjangoObjectType):

  class Meta:
    model = Movie
    
class ProducerType(DjangoObjectType):

  class Meta:
    model = Producer

class CharacterType(DjangoObjectType):

  class Meta:
    model = Character

class Character2Type(DjangoObjectType):
    class Meta:
        model = Character2

class FilmType(DjangoObjectType):
    class Meta:
        model = Film

class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
    
class Film2Type(DjangoObjectType):
    class Meta:
        model = Film2
    

class Query(object):

    movie = graphene.Field(MovieType,
        id=graphene.Int(),name=graphene.String())
    all_categories = graphene.List(CategoryType)
    all_movies = graphene.List(MovieType)
    category = graphene.Field(CategoryType,id=graphene.Int(), name=graphene.String())
    #me retorna lista de categorias con list
    #con field me retorna el json

    producer = graphene.Field(ProducerType, id=graphene.Int(), name=graphene.String(), last_name=graphene.String())
    character = graphene.Field(CharacterType,id=graphene.Int(), name=graphene.String(), color_hair=graphene.String())

    character2 = graphene.Field(Character2Type, id=graphene.Int(), name=graphene.String(), height=graphene.String(), mass=graphene.String(),
    hair_color=graphene.String(),skin_color=graphene.String(),eye_color=graphene.String(),birth_year=graphene.String(),gender=graphene.String(),homeworld=graphene.String())
    films = graphene.Field(FilmType, id=graphene.Int(), opening_crawl=graphene.String(),director=graphene.String())
    films2 = graphene.Field(Film2Type, id=graphene.Int(), opening_crawl=graphene.String(),director=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    
    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.select_related('category').all()

    
    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Movie.objects.select_related('category').get(pk=id)
        if name is not None:
            return Movie.objects.select_related('category').get(name=name)
        return None

    def resolve_character2(self,info,**kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Character2.objects.all()
    
    def resolve_films(self,info,**kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Movie.objects.select_related('character2').get(pk=id)


    

    def resolve_category(self, info, **kwargs):

        id = kwargs.get('id')

        if id is not None:
           return Category.objects.get(pk=id)
        else:
            return None  