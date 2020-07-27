from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)
  def __str__(self):
    return self.name

class Category1(models.Model):
  name = models.CharField(max_length=50, unique=True)
  def __str__(self):
    return self.name


class Category2(models.Model):
  name = models.CharField(max_length=50, unique=True)
  last_name = models.CharField(max_length=50, unique=True)
  def __str__(self):
    return self.name

class Movie2(models.Model):

  name = models.CharField(max_length=50)
  category = models.ForeignKey(Category2,  on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Movie(models.Model):

  name = models.CharField(max_length=50)
  year = models.IntegerField()
  rating = models.IntegerField()
  category = models.ForeignKey(Category,  on_delete=models.CASCADE)
  def __str__(self):
    return self.name +" - "+str(self.year)

class Movie1(models.Model):

  name = models.CharField(max_length=50)
  year = models.IntegerField()
  rating = models.IntegerField()
  category = models.ForeignKey(Category,  on_delete=models.CASCADE)
  def __str__(self):
    return self.name +" - "+str(self.year)

class Producer(models.Model):

  name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
  def __str__(self):
    return self.name +" - "+str(self.year)

class Character(models.Model):
  name = models.CharField(max_length=50)
  color_hair = models.CharField(max_length=50)
  movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
  def __str__(self):
    return self.name +" - "+str(self.year)


class Character2(models.Model):

    name = models.CharField(max_length=500)
    height = models.CharField(max_length=500)
    mass = models.CharField(max_length=20)
    hair_color = models.CharField(max_length=20)
    skin_color = models.CharField(max_length=20)
    eye_color = models.CharField(max_length=30)
    birth_year = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    homeworld = models.CharField(max_length=50)

class Film(models.Model):

    opening_crawl = models.CharField(max_length=1000)
    director = models.CharField(max_length=100)
    id_char = models.ForeignKey(Character,  on_delete=models.CASCADE)


class Planet(models.Model):

  name = models.CharField(max_length=50)
  poblation = models.IntegerField()
  film = models.ForeignKey(Film, on_delete=models.CASCADE, default='')


class Producer2(models.Model):
  name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  film_pro = models.ForeignKey(Film, on_delete=models.CASCADE)
  def __str__(self):
    return self.name +" - "+str(self.year)

class Film2(models.Model):

  opening_crawl = models.CharField(max_length=1000)
  director = models.CharField(max_length=100)
  character_id = models.ForeignKey(Character2,  on_delete=models.CASCADE)


class Personaje(models.Model):
  name = models.CharField(max_length=50, unique=True)
  last_name = models.CharField(max_length=50, unique=True)


class Pelicula(models.Model):
  name = models.CharField(max_length=50,unique=True)
  creditos = models.CharField(max_length=2000, unique=True)
  director = models.CharField(max_length=50, unique=True)
  personaje_id = models.ForeignKey(Personaje, on_delete=models.CASCADE)
