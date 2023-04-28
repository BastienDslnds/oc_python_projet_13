import pytest
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def user_one():
    user = User.objects.create_user(
        username="BastienDslnds",
        first_name="Bastien",
        last_name="Deslandes",
        email="bastien@test.com",
        password="Bastien10",
    )
    return user


@pytest.fixture
def profile_one(user_one):
    profile = Profile.objects.create(user=user_one, favorite_city="Rome")
    return profile
