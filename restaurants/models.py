from django.db import models
from rest_framework.exceptions import ValidationError


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


def validate_dishes_format(value) -> None:
    valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    for day in value.keys():
        if day.lower() not in valid_days:
            raise ValidationError(f"'{day}' is not a valid day name. Valid day names are: {', '.join(valid_days)}")


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")
    date = models.DateField(auto_now_add=True)
    dishes = models.JSONField(validators=[validate_dishes_format])

    class Meta:
        unique_together = ("restaurant", "date")

    def __str__(self) -> str:
        if self.restaurant.name[-1] != "s":
            return self.restaurant.name + "'s menu"
        else:
            return self.restaurant.name + "' menu"
