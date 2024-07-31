from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarsModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at')

    # def validate(self, data):
    #     if data['price'] == data['year']:
    #         raise ValidationError({'details': 'Error price eq year'})
    #     return data

    # def validate_year(self, year):
    #     if year == 2002:
    #         raise ValidationError({'details': 'year eq 2002 '})
    #     return year
