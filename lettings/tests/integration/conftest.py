import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address_one():
    address = Address.objects.create(
        number=52,
        street="Gaite Street",
        city="Paris",
        state="France",
        zip_code=75014,
        country_iso_code="FR",
    )

    return address


@pytest.fixture
def address_two():
    address = Address.objects.create(
        number=101,
        street="Montparnasse Street",
        city="Paris",
        state="France",
        zip_code=75014,
        country_iso_code="FR",
    )

    return address


@pytest.fixture
def letting_one(address_one):
    letting = Letting.objects.create(
        title="Mercure quarter", address=address_one
    )

    return letting


@pytest.fixture
def letting_two(address_two):
    letting = Letting.objects.create(
        title="Montparnasse quarter", address=address_two
    )

    return letting
