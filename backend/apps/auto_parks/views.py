from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.permissions.is_admin_or_write_only import IsAdminOrWriteOnly

from apps.auto_parks.models import AutoPark
from apps.auto_parks.serializers import AutoParksSerializer
from apps.cars.serializers import CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class AutoParksListCreateView(ListCreateAPIView):
    """"
        get:
             get all AutoParks info,
        post:
            create AutoPark
    """
    serializer_class = AutoParksSerializer
    queryset = AutoPark.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)

@method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class AutoParksAddCarView(GenericAPIView):
    """"
        get:
             get all AutoParks info,
        post:
            create AutoPark with car
    """
    queryset = AutoPark.objects.all()
    serializer_class = CarSerializer

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParksSerializer(auto_park)
        return Response(ap_serializer.data, status=status.HTTP_201_CREATED)