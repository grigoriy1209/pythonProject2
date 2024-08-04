from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarsModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'photo', 'created_at', 'updated_at')


class CarFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}