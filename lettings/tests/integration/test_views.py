import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_index_page_is_online(client):
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
