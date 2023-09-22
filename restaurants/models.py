from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")
    date = models.DateField(auto_now_add=True)
    dishes = models.JSONField()

    class Meta:
        unique_together = ("restaurant", "date")
