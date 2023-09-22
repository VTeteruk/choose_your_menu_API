from rest_framework import routers

from restaurants.views import RestaurantViewSet, MenuViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)

urlpatterns = router.urls

app_name = "restaurants"
