from django.urls import path
from rest_framework import routers

from restaurants.views import RestaurantViewSet, MenuViewSet, vote_for_menu

router = routers.DefaultRouter()
router.register(r"restaurants", RestaurantViewSet)
router.register(r"menus", MenuViewSet)

urlpatterns = [
    path("menus/<int:pk>/vote/", vote_for_menu)
] + router.urls

app_name = "dishes"
