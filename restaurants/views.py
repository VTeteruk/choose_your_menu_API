from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import restaurants.models
from restaurants.models import Menu, Restaurant
from restaurants.serializers import (
    MenuSerializer,
    RestaurantSerializer,
    MenuListSerializer,
)


class MenuViewSet(ModelViewSet):
    """Show menu for current day if is in list format or all menu if is in retrieve format
    Dishes must be a dict in such format: {'day': 'dish, dish', 'day': 'dish'}
    """

    queryset = Menu.objects.annotate(votes_count=Count('employees'))
    serializer_class = MenuSerializer

    def get_serializer_class(self) -> serializers:
        if self.action == "list":
            return MenuListSerializer
        return MenuSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


@api_view(["POST"])
def vote_for_menu(request, pk: int) -> Response:
    if request.method == "POST":
        try:
            employee = get_user_model().objects.get(id=request.user.id)
            employee.votes = Menu.objects.get(id=pk)
        except restaurants.models.Menu.DoesNotExist:
            return Response({"message": "No such menu index"})
        employee.save()
        return Response({"message": "You have voted successfully"})
    return Response({"message": "Method Post is allowed only"})
