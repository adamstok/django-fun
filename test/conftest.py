import pytest
from django.contrib.contenttypes.models import ContentType
from django.test import Client
from handling.models import ApartmentsRooms,ApartmentsPics,Apartments,Payments,Renters
from normalview.models import Messages
from django.contrib.auth.models import User,Permission

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user():
    user = User(username='test')
    user.set_password('test')
    user.save()
    # p = Permission.objects.get(codename='view_genre')
    # p1 = Permission.objects.get(codename='add_genre')
    # p2 = Permission.objects.get(codename='change_genre')
    # contenttype = ContentType.objects.get(model='genre')
    # permissions = Permission.objects.filter(content_type=contenttype)
    # user.user_permissions.set(permissions)
    # user.user_permissions.add(p) # jezeli chcemy dodawac uzytkownika z uprawnieniami, jak w views mamy permissiorequiredmixin
    # user.user_permissions.add(p1)
    # user.user_permissions.add(p2)
    user.save()
    return user
#
# @pytest.fixture
# def genre():
#     g = [Genre.objects.create(name='Kryminał')]
#     g.append(Genre.objects.create(name='Horror'))
#     g.append(Genre.objects.create(name='SCI-FI'))
#     return g
#
# @pytest.fixture
# def authors():
#     a = [Author.objects.create(first_name='adada',last_name='fefefe',year_of_birth=2019)]
#     return a