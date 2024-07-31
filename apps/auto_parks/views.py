from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoPark
from apps.auto_parks.serializers import AutoParksSerializer
from apps.cars.serializers import CarSerializer


class AutoParksListCreateView(ListCreateAPIView):
    serializer_class = AutoParksSerializer
    queryset = AutoPark.objects.all()


class AutoParksAddCarView(GenericAPIView):
    queryset = AutoPark.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParksSerializer(auto_park)
        return Response(ap_serializer.data, status=status.HTTP_201_CREATED)