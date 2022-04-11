import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, last_name",
    (
        ("Paulo", "Coelho"),
        ("Haruki", "Murakami"),
        ("Jordi", "Rosado")
    )
)

def test_author_name():
    author = Author.objects.create(name = "nombre", last_name = "apellido")
    print("This is my authors name: ", author.name)
    assert author.last_name == apellido
    author.delete()


# @pytest.mark.django_db
# def test_author_with_monkey(monkeypatch):
#     author = Author.objects.create(name = "nombre", last_name = "apellido")
#     def model_count_mock():
#         return 4

#     monkeypatch.setattribute(author.objects.all(), "count", model_count_mock)
#     assert Author.objects.all().count() == 4
#     print("Haciendo el monkeypatch")