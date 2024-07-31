from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from core.paginations import PagePagination

from apps.cars.filter import CarFilter
from apps.cars.models import CarsModel
from apps.cars.serializers import CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.less_then_year(2000)
    filterset_class = CarFilter


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()










