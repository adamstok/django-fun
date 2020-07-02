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

# @pytest.mark.django_db
# def test_publishers(client,user):
#     client.login(username='test',password='test')
#     response = client.get('/publishers/')
#     assert response.status_code == 200

@pytest.mark.django_db
def test_payments(client,user):#,genre):
    client.login(username='test',password='test')
    response = client.get('/payments/')
    #response.context['objects'] = w views addGenre przekazujemy na stronie 'objects' w context
    assert response.status_code == 200
    #assert len(response.context['objects']) == 2
    # for i in range(len(genre)):
    #     assert genre[i] in response.context['objects']

@pytest.mark.django_db
def test_pics(client,user):#,authors):
    client.login(username='test',password='test')
    response = client.get('/upload/')
    #response.context['objects'] = w views addGenre przekazujemy na stronie 'objects' w context
    assert response.status_code == 200
    # assert len(response.context['objects']) == 1
    # for i in range(len(authors)):
    #      assert authors[i] in response.context['objects']


@pytest.mark.django_db
def test_messages(client,user):
    #client.login(username='test',password='test')
    response = client.get('/message/')
    assert response.status_code == 200