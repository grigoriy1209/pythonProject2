from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.cars.filter import CarFilter
from apps.cars.models import CarsModel
from apps.cars.serializers import CarFotoSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarsListView(ListAPIView):
    """
    Get all cars
    """
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
      get:
         get car details
      put:
        update car
      patch:
        partial update car
      delete:
        delete car
    """
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)


class CarAddFotoView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CarFotoSerializer
    queryset = CarsModel.objects.all()
    http_method_names = ('put', )

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)

