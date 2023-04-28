import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_index_page_is_online(client):
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_lettings_index_context_is_ok(client, letting_one, letting_two):
    response = client.get(reverse("lettings_index"))

    letting_one = response.context['lettings_list'].get(pk=letting_one.id)
    letting_two = response.context['lettings_list'].get(pk=letting_two.id)

    assert letting_one.title == "Mercure quarter"
    assert letting_two.title == "Montparnasse quarter"


@pytest.mark.django_db
def test_letting_page_is_online(client, letting_one):
    response = client.get(reverse("letting", args=[letting_one.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_page_context_is_ok(client, letting_one):
    response = client.get(reverse("letting", args=[letting_one.id]))

    assert response.context['title'] == "Mercure quarter"
    assert response.context['address'].street == "Gaite Street"
