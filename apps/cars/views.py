from typing import Type

from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.paginations import PagePagination

from apps.cars.filter import CarFilter
from apps.cars.models import CarsModel
from apps.cars.serializers import CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user, '!!!!!!!!!!!!!!')
        return super().get_queryset()


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)












