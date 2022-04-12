import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
    "nombre, apellido",
    (
        ("Paulo", "Coelho"),
        ("Haruki", "Murakami"),
        ("Jordi", "Rosado")
    )
)

def test_author_name(nombre, apellido):
    author = Author.objects.create(name = nombre, last_name = apellido)
    print("This is my authors name: ", author.name)
    assert author.last_name == apellido
    author.delete()


@pytest.mark.django_db
def test_author_with_monkey(monkeypatch):
    author = Author.objects.create(name = "nombre", last_name = "apellido")

    class AuthorQuerysetMock():
        def __init__(self):
          self.some_value = 1

        def count(self):
          return 4

    def model_count_mock():
      return AuthorQuerysetMock()

    monkeypatch.setattr(Author.objects, "all", model_count_mock)

    assert Author.objects.all().count() == 4
    print("Haciendo el monkeypatch")
    

    # def model_count_mock():
    #     return 4
    # print(dir(Author.objects))
    # print(type(Author.objects))
    # print(type(Author.objects.all()))
    # print(dir(Author.objects.all()))    
    # monkeypatch.setattr(Author.objects, "count", model_count_mock)

    # assert Author.objects.count() == 4
    # print("haciendo el monkeypatch")




# Homework Tests

# Language Tests

@pytest.mark.django_db
@pytest.mark.parametrize(
    "lenguaje", (
        ("English"),
        ("Chinese"),
        ("Portuguese")
    )
)

def test_book_language(lenguaje):
    language = Language.objects.create(language = lenguaje)
    print("These are my languages: ", language.language)
    assert language.language == lenguaje
    language.delete()

@pytest.mark.django_db
@pytest.mark.parametrize(
    "lenguaje", (
        ("English"),
        ("Chinese"),
        ("Portuguese")
    )
)

def test_book_language_is_valid(lenguaje):
  languageList = ['English', 'Chinese', 'Japanese', 'Portuguese', 'Spanish']
  language = Language.objects.create(language = lenguaje)
  print(language.language, 'exist in', languageList)
  assert language.language in languageList
  language.delete()

@pytest.mark.django_db
@pytest.mark.parametrize(
    "lenguaje", (
        ("English"),
        ("Chinese"),
        ("Portuguese")
    )
)

def test_book_language_type(lenguaje):
  language = Language.objects.create(language = lenguaje)
  assert type(language.language) is not int
  assert type(language.language) is str
  language.delete()




@pytest.mark.django_db
@pytest.mark.parametrize(
  'genero',
  (
    ('Programming'),
    ('Self help'),
    ('History'),
  )
)


def test_book_genre(genero):
  genre = Genre.objects.create(genre = genero) 
  print('This is my gender parameter: ', genre.genre) 
  assert genre.genre == genero 
  assert Genre.objects.count() == 1
  genre.delete()
  assert Genre.objects.count() == 0

@pytest.mark.django_db
@pytest.mark.parametrize(
  'genero',
  (
    ('Fiction'),
    ('Engineering'),
    ('Programming'),
  )
)


def test_book_genre_in_list(genero):
  genreList = ['Programming', 'History', 'Sports', 'Educational', 'Engineering', 'Horror', 'Thriller', 'Fiction']
  genre = Genre.objects.create(genre = genero)
  print(genre.genre, 'exist in', genreList)
  assert genre.genre in genreList
  genre.delete()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'genero',
    (
        ('Garbage'),
        ('XD'),
        ('Not a genre'),
    )
)


def test_book_genre_is_valid(genero):
    genreList = ['Programming', 'History', 'Sports', 'Educational', 'Engineering', 'Horror', 'Thriller', 'Fiction']
    genre = Genre.objects.create(genre = genero)
    print(genre.genre, 'not exist in', genreList)
    assert genre.genre not in genreList
    genre.delete()

@pytest.mark.django_db
@pytest.mark.parametrize(
  'genero',
  (
    ('Fiction'),
    ('Engineering'),
    ('Programming'),
  )
)


def test_genre_type(genero):
  genre = Genre.objects.create(genre=genero)
  print('Genre:', genre.genre, 'type: ', type(genre.genre))
  assert type(genre.genre) is not int
  assert type(genre.genre) is str
  genre.delete() 