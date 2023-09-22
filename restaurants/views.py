from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import restaurants.models
from restaurants.models import Menu, Restaurant
from restaurants.serializers import MenuSerializer, RestaurantSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


@api_view(["GET"])
def vote_for_menu(request, pk: int) -> Response:
    if request.method == "GET":
        try:
            employee = get_user_model().objects.get(id=request.user.id)
            employee.votes = Menu.objects.get(id=pk)
        except restaurants.models.Menu.DoesNotExist:
            return Response({"message": "No such menu index"})
        employee.save()
        return Response({"message": "You have voted successfully"})
    return Response({"message": "Method Post is allowed only"})
