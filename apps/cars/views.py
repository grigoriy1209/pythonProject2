from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from core.paginations import PagePagination

from apps.cars.filter import CarFilter
from apps.cars.models import CarsModel
from apps.cars.serializers import CarSerializer


class CarsListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    # pagination_class = PagePagination
    queryset = CarsModel.objects.all()
    filterset_class = CarFilter

    # def get_queryset(self):
    #     return car_filter(self.request.query_params)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()










