from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
# router.register(r'books', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'language', views.LanguageViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'authors', views.BooksAuthorsViewSet)
router.register(r'genres', views.BooksGenresViewSet)
router.register(r'languages', views.BooksLanguagesViewSet)
router.register(r'thing', views.ThingViewSet)
router.register(r'', views.BookViewSet)
# La url vacia tiene que ir al final.

urlpatterns = [
	path('', include(router.urls)),
]