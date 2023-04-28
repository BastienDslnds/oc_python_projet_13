import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_page_is_online(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_template_is_ok(client):
    response = client.get(reverse("index"))

    assert b'Welcome to Holiday Homes' in response.content
