from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "is_staff")
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("username", "first_name", "last_name", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
