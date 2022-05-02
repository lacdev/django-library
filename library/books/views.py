from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from .serializers import *
import base64
from rest_framework.response import Response
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser, JSONParser
from rest_framework import pagination

from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.vary import vary_on_headers

from rest_framework import status

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'p'

class CustomPaginationOffset(pagination.LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 10

class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().order_by('id')
    serializer_class = ThingSerializer
    permission_classes = []

# @method_decorator(cache_page(60*60, key_prefix="author"))
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = []
    # pagination_class = CustomPagination

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = []

class BooksAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorsSerializer
    permission_classes = []

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = []

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = []

class BooksGenresViewSet(viewsets.ModelViewSet):
    queryset = BooksGenres.objects.all()
    serializer_class = BooksGenresSerializer
    permission_classes = []

class BooksLanguagesViewSet(viewsets.ModelViewSet):
    queryset = BooksLanguages.objects.all()
    serializer_class = BooksLanguagesSerializer
    permission_classes = []