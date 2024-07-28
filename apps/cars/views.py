from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filter import car_filter
from apps.cars.models import CarsModel
from apps.cars.serializers import CarSerializer


# class CarsListCreateView(GenericAPIView):
#
#     def get(self, *args, **kwargs):
#         # qs = CarsModel.objects.filter(brand__in=['bmw', 'opel'], year__gte=2020).order_by('-year').reverse()
#         # qs = CarsModel.objects.filter(brand__in=['bmw', 'opel'], year__gte=2020).order_by('year')
#         # qs = CarsModel.objects.filter(Q(brand__in=['opel','bmw']) | Q(price=2000)).exclude(brand='bmw')
#         qs = CarsModel.objects.all()
#         # res = [model_to_dict(car) for car in cars]
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarsRetrieveUpdateDestroyView(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarsModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         # pk = self.kwargs['pk']
#         # try:
#         #     car = CarsModel.objects.get(pk=pk)
#         # except CarsModel.DoesNotExist:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         # pk = self.kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarsModel.objects.get(pk=pk)
#         # except CarsModel.DoesNotExist:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # pk = self.kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarsModel.objects.get(pk=pk)
#         # except CarsModel.DoesNotExist:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         serializer = CarSerializer(car, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = self.kwargs['pk']
#         # try:
#         #     car = CarsModel.objects.get(pk=pk)
#         #     car.delete()
#         # except CarsModel.DoesNotExist:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CarsListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     serializer_class = CarSerializer
#     # queryset = CarsModel.objects.all()
#
#     def get_queryset(self):
#         return car_filter(self.request.query_params)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#
# class CarsRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarsModel.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


class CarsListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()










