from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length = 128)
    image = models.TextField(null = False)

class Author(models.Model):
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null = True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Language(models.Model):
    language = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.language}'

class Genre(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.genre}'

class Book(models.Model):
    name = models.CharField(max_length = 256)
    publish_year = models.SmallIntegerField()
    pages = models.SmallIntegerField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null = True)
    authors = models.ManyToManyField(Author, through='BooksAuthors')
    language = models.ManyToManyField(Language, through='BooksLanguages')
    genre = models.ManyToManyField(Genre, through='BooksGenres')

    def __str__(self):
        return f'{self.name}'

class BooksAuthors(models.Model):
    book = models.ForeignKey(Book, related_name='BookWithAuthors', on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, related_name='AuthorWithBooks', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.book} by {self.author}'

class BooksGenres(models.Model):
    book = models.ForeignKey(Book, related_name='BookWithGenres', on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, related_name='GenreWithBooks', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.book} of {self.genre} genre'

class BooksLanguages(models.Model):
    book = models.ForeignKey(Book, related_name='BookWithLanguages', on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Language, related_name='LanguageWithBooks', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.book} written in {self.language}'