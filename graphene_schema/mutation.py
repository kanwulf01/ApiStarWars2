import graphene
from movies.models import *
from .types import *

class CreateCategoryMutation(graphene.Mutation):
  class Input:
    name = graphene.String()
  name = graphene.Field(CategoryType)
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    obj = Category.objects.create(name=name)
    return CreateCategoryMutation(name=obj)


class CreateCategory1Mutation(graphene.Mutation):
  class Input:
    name = graphene.String()
  name = graphene.Field(Category1Type)
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    obj = Category1.objects.create(name=name)
    return CreateCategory1Mutation(name=obj)


class CreateCategory2Mutation(graphene.Mutation):
  class Input:
    name = graphene.String()
  name = graphene.Field(Category2Type)
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    last_name = kwargs.get('last_name','').strip()
    obj = Category2.objects.create(name=name,last_name=last_name)
    return CreateCategory2Mutation(name=obj)

class CreateCharacter2Mutation(graphene.Mutation):
  class Input:
    name = graphene.String()
    height = graphene.String()
    mass = graphene.String()
    hair_color = graphene.String()
    skin_color = graphene.String()
    eye_color = graphene.String()
    birth_year = graphene.String()
    gender = graphene.String()
    homeworld = graphene.String()
  name = graphene.Field(Character2Type)
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    height = kwargs.get('height', '').strip()
    mass = kwargs.get('mass', '').strip()
    hair_color = kwargs.get('hair_color', '').strip()
    skin_color = kwargs.get('skin_color', '').strip()
    eye_color = kwargs.get('eye_color', '').strip()
    birth_year = kwargs.get('birth_year', '').strip()
    gender = kwargs.get('gender', '').strip()
    homeworld = kwargs.get('homeworld', '').strip()
    _obj = Character2.objects.create(name=name,height=height,
    mass=mass,hair_color=hair_color,skin_color=skin_color,eye_color=eye_color,birth_year=birth_year,gender=gender,homeworld=homeworld)
    return CreateCategoryMutation(name=_obj)


class CreateFilmMutation(graphene.Mutation):

  class Input(object):


    opening_crawl = graphene.String()
    director = graphene.String()
    id_char = graphene.Int()
  name = graphene.Field(FilmType)
  @staticmethod
  def mutate(root,info, **kwargs):

    opening_crawl = kwargs.get('opening_crawl').strip()
    director = kwargs.get('director').strip()
    id_char = kwargs.get('id_char', 0)
    _obj = Film.objects.create(opening_crawl=opening_crawl,director=director,id_char=1)
    return CreateFilmMutation(name=_obj)


class CreateFilm2Mutation(graphene.Mutation):

  class Input:


    opening_crawl = graphene.String()
    director = graphene.String()
    character_id = graphene.Int()
  name = graphene.Field(Film2Type)
  @staticmethod
  def mutate(root,info, **kwargs):
    opening_crawl = kwargs.get('opening_crawl').strip()
    director = kwargs.get('director').strip()
    character_id = kwargs.get('character_id', 0)
    _obj = Film2.objects.create(opening_crawl=opening_crawl,director=director,character_id=1)
    return CreateFilm2Mutation(name=_obj)



class CreateMovieMutation(graphene.Mutation):
  class Input(object):
    name = graphene.String()
    year = graphene.Int()
    rating = graphene.Int()
    category_id = graphene.Int()
  name = graphene.Field(MovieType)
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    year = kwargs.get('year', 0)
    rating = kwargs.get('rating', 0)
    category_id = kwargs.get('category_id', 0)

    obj = Movie.objects.create(name=name,year=year,
            rating=rating,category_id=category_id)
    return CreateMovieMutation(name=obj)

class CreateMovie1Mutation(graphene.Mutation):
  class Input(object):
    name = graphene.String()
    year = graphene.Int()
    rating = graphene.Int()
    category_id = graphene.Int()
  name = graphene.Field(Movie1Type)
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    year = kwargs.get('year', 0)
    rating = kwargs.get('rating', 0)
    category_id = kwargs.get('category_id', 0)

    obj = Movie1.objects.create(name=name,year=year,
            rating=rating,category_id=category_id)
    return CreateMovie1Mutation(name=obj)

class CreateMovie2Mutation(graphene.Mutation):
  class Input(object):
    name = graphene.String()
    
    category_id = graphene.Int()
  name = graphene.Field(Movie2Type)
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    
    category_id = kwargs.get('category_id', 0)

    obj = Movie2.objects.create(name=name,category_id=category_id)
    return CreateMovie2Mutation(name=obj)


class CreateCharacterMutation(graphene.Mutation):

  class Input:


    name = graphene.String()
    color_hair = graphene.String()
    movie_id = graphene.Int()
  name = graphene.Field(CharacterType)
    
  @staticmethod

  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    color_hair = kwargs.get('color_hair', '').strip()
    movie_id = kwargs.get('movie_id', 0)
    obj = Character.objects.create(name=name,last_name=color_hair, movieID=movie_id)
    return CreateCharacterMutation(name=obj)



class CreateProducerMutation(graphene.Mutation):



  class Input(object):

    name = graphene.String()
    last_name = graphene.String()
    movieID = graphene.Int()
  name = graphene.Field(ProducerType)
    
  @staticmethod
  def mutate(root, info, **kwargs):
    name = kwargs.get('name', '').strip()
    last_name = kwargs.get('last_name', '').strip()
    movieID = kwargs.get('movieID', 0)
    obj = Producer.objects.create(name=name,last_name=last_name,
          movieID=movieID)
    return CreateProducerMutation(name=obj)


class CreatePersonajeMutation(graphene.Mutation):
  class Input(object):

    name = graphene.String()
    last_name = graphene.String()
  name = graphene.Field(PersonajeType)
  @staticmethod
  def mutate(root,info,**kwargs):
    name = kwargs.get('name', '').strip()
    last_name = kwargs.get('last_name', '').strip()
    obj = Personaje.objects.create(name=name,last_name=last_name)
    return CreatePersonajeMutation(name=obj)

class CreatePeliculaMutation(graphene.Mutation):
  class Input(object):
    name = graphene.String()
    creditos = graphene.String()
    director = graphene.String()
    personaje_id = graphene.Int()
  name = graphene.Field(PeliculaType)
  @staticmethod
  def mutate(root,info,**kwargs):
    name = kwargs.get('name', '').strip()
    creditos = kwargs.get('creditos', '').strip()
    director = kwargs.get('director', '').strip()
    personaje_id = kwargs.get('personaje_id',0)
    obj = Pelicula.objects.create(name=name,director=director,creditos=creditos,personaje_id=1)
    return CreatePeliculaMutation(name=obj)

class Mutation(graphene.AbstractType):
  create_category = CreateCategoryMutation.Field()
  create_movie = CreateMovieMutation.Field()
  create_producer = CreateProducerMutation.Field()
  create_character = CreateCharacterMutation.Field()
  create_character2 = CreateCharacter2Mutation.Field()
  create_film = CreateFilmMutation.Field()
  create_film2 = CreateFilm2Mutation.Field()
  create_pelicula = CreatePeliculaMutation.Field()
  create_personaje = CreatePersonajeMutation.Field()
  create_category1 = CreateCategory1Mutation.Field()
  create_movie1 = CreateMovie1Mutation.Field()
  create_category2 = CreateCategory2Mutation.Field()
  create_movie2 = CreateMovie2Mutation.Field()
  