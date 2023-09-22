import datetime

from rest_framework.viewsets import ModelViewSet

from restaurants.models import Menu, Restaurant
from restaurants.serializers import MenuSerializer, RestaurantSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
