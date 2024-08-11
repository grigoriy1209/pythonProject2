from django.urls import path

from apps.cars.views import CarAddFotoView, CarsListView, CarsRetrieveUpdateDestroyView

urlpatterns = [
  path('', CarsListView.as_view()),
  path('/<int:pk>', CarsRetrieveUpdateDestroyView.as_view()),
  path('/<int:pk>/photo', CarAddFotoView.as_view()),

  # path('/test', TestEmailView.as_view())

 ]
