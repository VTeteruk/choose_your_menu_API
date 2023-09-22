from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class CreateEmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny,)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Show information about current user"""

    serializer_class = EmployeeSerializer

    def get_object(self) -> Employee:
        return get_user_model().objects.get(id=self.request.user.id)
