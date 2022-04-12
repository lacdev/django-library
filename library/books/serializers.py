from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'last_name']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'name', 'publish_year', 'pages', 'price', 'created_at', 'updated_at', 'language', 'genre', 'authors']
        
class BooksAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthors
        fields = ['id', 'book', 'author']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language']

class BooksGenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksGenres
        fields = ['id', 'book', 'genre']

class BooksLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguages
        fields = ['id', 'book', 'language']