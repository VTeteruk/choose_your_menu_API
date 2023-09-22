from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from employees.views import CreateEmployeeView, EmployeeDetailView

urlpatterns = [
    path("register/", CreateEmployeeView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", EmployeeDetailView.as_view(), name="user-details"),
]

app_name = "employees"
