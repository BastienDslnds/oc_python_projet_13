import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index_page_is_online(client):
    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_index_context_is_ok(client, profile_one):
    response = client.get(reverse("profiles_index"))

    profile_one = response.context['profiles_list'].get(pk=profile_one.id)

    assert profile_one.favorite_city == "Rome"
    assert profile_one.user.username == "BastienDslnds"
