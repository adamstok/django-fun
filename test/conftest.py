import pytest
from django.test import Client
from django.contrib.auth.models import User

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user():
    user = User(username='test')
    user.set_password('test')
    user.save()
    user.save()
    return user
