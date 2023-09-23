import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from restaurants.models import Restaurant, Menu


def create_user() -> Employee:
    return get_user_model().objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="testpassword",
        first_name="Test",
        last_name="User",
        position="Tester",
    )


@pytest.mark.django_db
def test_create_employee() -> None:
    client = APIClient()
    url = reverse("employees:register")
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword",
        "first_name": "Test",
        "last_name": "User",
        "position": "Tester",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_employee_detail_view() -> None:
    user = create_user()

    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("employees:user-details")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == "testuser"


@pytest.mark.django_db
def test_employee_serializer() -> None:
    user = create_user()

    serializer = EmployeeSerializer(instance=user)
    assert serializer.data["username"] == "testuser"
    assert serializer.data["position"] == "Tester"


@pytest.mark.django_db
def test_vote_for_menu() -> None:
    restaurant = Restaurant.objects.create(name="Test Restaurant")
    menu = Menu.objects.create(restaurant=restaurant, dishes={"monday": "Test Dish"})

    user = create_user()

    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse("dishes:vote_for_menu", kwargs={"pk": menu.id})
    response = client.post(url)

    assert response.status_code == status.HTTP_200_OK

    user.refresh_from_db()
    assert user.votes == menu


@pytest.mark.django_db
def test_vote_for_menu_for_two_menus() -> None:
    restaurant1 = Restaurant.objects.create(name="Test Restaurant 1")
    restaurant2 = Restaurant.objects.create(name="Test Restaurant 2")
    menu1 = Menu.objects.create(restaurant=restaurant1, dishes={"monday": "Test Dish"})
    menu2 = Menu.objects.create(restaurant=restaurant2, dishes={"friday": "Test Dish"})

    user = create_user()

    client = APIClient()
    client.force_authenticate(user=user)

    url1 = reverse("dishes:vote_for_menu", kwargs={"pk": menu1.id})
    url2 = reverse("dishes:vote_for_menu", kwargs={"pk": menu2.id})
    response1 = client.post(url1)
    response2 = client.post(url2)

    assert response1.status_code == status.HTTP_200_OK
    assert response2.status_code == status.HTTP_200_OK

    user.refresh_from_db()
    assert user.votes == menu2
