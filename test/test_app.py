import pytest


@pytest.mark.django_db
def test_rooms(client,user):
    client.login(username='test',password='test')
    response = client.get('/rooms/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_apartments(client,user):
    client.login(username='test',password='test')
    response = client.get('/apartments/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_renters(client,user):
    client.login(username='test',password='test')
    response = client.get('/renters/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_payments(client,user):
    client.login(username='test',password='test')
    response = client.get('/payments/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_pics(client,user):
    client.login(username='test',password='test')
    response = client.get('/upload/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_messages(client):
    response = client.get('/message/')
    assert response.status_code == 200