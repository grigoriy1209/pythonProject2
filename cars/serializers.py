from rest_framework import serializers

from cars.models import CarsModel


# class CarSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     brand = serializers.CharField(max_length=255)
#     price = serializers.IntegerField()
#     year = serializers.IntegerField()
#
#     def create(self, validated_data: dict):
#         car = CarsModel.objects.create(**validated_data)
#         return car
#
#     def update(self, instance, validated_data: dict):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#             instance.save()
#             return instance

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')
