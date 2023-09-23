import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from employees.tests.test_employees import create_user
from restaurants.models import Restaurant, Menu


@pytest.fixture
def create_authenticated_client() -> APIClient:
    user = create_user()

    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def create_restaurant() -> Restaurant:
    return Restaurant.objects.create(name="Test Restaurant")


@pytest.mark.django_db
def test_create_menu(create_authenticated_client, create_restaurant) -> None:
    client = create_authenticated_client
    url = reverse("dishes:menu-list")
    data = {
        "restaurant": create_restaurant.id,
        "dishes": {"monday": "Test Dish"},
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_update_menu(create_authenticated_client, create_restaurant) -> None:
    # Create a menu
    menu = Menu.objects.create(
        restaurant=create_restaurant, dishes={"monday": "Test Dish"}
    )

    client = create_authenticated_client
    url = reverse("dishes:menu-detail", args=[menu.id])
    updated_data = {
        "restaurant": create_restaurant.id,
        "dishes": {"monday": "Updated Dish"},
    }
    response = client.put(url, updated_data, format="json")
    assert response.status_code == status.HTTP_200_OK

    menu.refresh_from_db()
    assert menu.dishes["monday"] == "Updated Dish"


@pytest.mark.django_db
def test_retrieve_menu(create_authenticated_client, create_restaurant) -> None:
    menu = Menu.objects.create(
        restaurant=create_restaurant, dishes={"monday": "Test Dish"}
    )

    client = create_authenticated_client
    url = reverse("dishes:menu-detail", args=[menu.id])
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["dishes"]["monday"] == "Test Dish"


@pytest.mark.django_db
def test_delete_menu(create_authenticated_client, create_restaurant) -> None:
    menu = Menu.objects.create(
        restaurant=create_restaurant, dishes={"monday": "Test Dish"}
    )

    client = create_authenticated_client
    url = reverse("dishes:menu-detail", args=[menu.id])
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT

    with pytest.raises(Menu.DoesNotExist):
        menu.refresh_from_db()


@pytest.mark.django_db
def test_create_menu_with_invalid_data(create_authenticated_client) -> None:
    client = create_authenticated_client
    url = reverse("dishes:menu-list")
    data = {
        "restaurant": 999,
        "dishes": {"M": "Test Dish"},
    }
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
