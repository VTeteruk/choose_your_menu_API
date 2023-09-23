import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from employees.models import Employee


def create_user() -> Employee:
    return get_user_model().objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="testpassword",
        first_name="Test",
        last_name="User",
        position="Tester",
    )


@pytest.fixture
def authenticated_client() -> APIClient:
    user = create_user()  # Call create_user function to create a user instance

    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.mark.django_db
def test_create_authenticated_restaurant(authenticated_client) -> None:
    url = reverse("dishes:restaurant-list")
    data = {
        "name": "Test Restaurant",
    }
    response = authenticated_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_authenticated_restaurant_twice(authenticated_client) -> None:
    url = reverse("dishes:restaurant-list")
    data = {
        "name": "Test Restaurant",
    }
    authenticated_client.post(url, data, format="json")
    response = authenticated_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_create_unauthenticated_restaurant() -> None:
    client = APIClient()
    url = reverse("dishes:restaurant-list")
    data = {
        "name": "Test Restaurant",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
