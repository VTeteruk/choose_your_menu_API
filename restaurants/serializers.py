import datetime

from rest_framework import serializers
from restaurants.models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

    def to_representation(self, instance):
        today = datetime.date.today()
        today_dishes = instance.dishes.get(today.strftime("%A").lower())

        data = {
            "id": instance.id,
            "restaurant": instance.restaurant.name,
            "date": datetime.date.today(),
            "dishes": today_dishes if today_dishes else "No dishes for today",
        }
        return data

    def update(self, instance, validated_data):
        if "restaurant" in validated_data:
            raise serializers.ValidationError("Changing the restaurant of a menu is not allowed.")

        return super().update(instance, validated_data)
