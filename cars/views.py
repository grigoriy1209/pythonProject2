from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from cars.models import CarsModel


class CarsListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarsModel.objects.all()
        res = [model_to_dict(car) for car in cars]
        return Response(res, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarsModel.objects.create(**data)
        car_dict = model_to_dict(car)
        return Response(car_dict, status.HTTP_201_CREATED)


class CarsRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs['pk']
        try:
            car = CarsModel.objects.get(pk=pk)
        except CarsModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(car), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = self.kwargs['pk']
        data = self.request.data
        try:
            car = CarsModel.objects.get(pk=pk)
        except CarsModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        car.brand = data['brand']
        car.price = data['price']
        car.year = data['year']
        car.save()
        return Response(model_to_dict(car), status.HTTP_200_OK)

    # def patch(self, *args, **kwargs):
    #     return Response({'message': 'Hello World! patch'})

    def delete(self, *args, **kwargs):
        pk = self.kwargs['pk']
        try:
            car = CarsModel.objects.get(pk=pk)
            car.delete()
        except CarsModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
