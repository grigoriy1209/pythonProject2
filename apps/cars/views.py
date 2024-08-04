from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.permissions.is_super_user_permission import IsSuperUserPermission

from apps.cars.filter import CarFilter
from apps.cars.models import CarsModel
from apps.cars.serializers import CarFotoSerializer, CarSerializer


class CarsListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
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




