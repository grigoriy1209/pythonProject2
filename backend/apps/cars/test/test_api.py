from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.dataclasses.user_dataclass import User

from apps.cars.models import CarsModel

UserModel = get_user_model()


class CarApiTest(APITestCase):
    def setUp(self):
        self.car1 = CarsModel.objects.create(
            brand="BMW",
            price=2000,
            year=2000,
            body_type="Sedan"
        )
        self.car2 = CarsModel.objects.create(
            brand="Audy",
            price=2000,
            year=2000,
            body_type="Jeep"
        )

    def _authenticate(self):
        email = 'admin@gmail.com'
        password = 'P@$$word1'
        self.client.post(reverse('users-list_create'), {
            'email': email,
            'password': password,
            'profile': {
                "name": "Max",
                "surname": "Popov",
                "age": 30
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()
        res = self.client.post(reverse('auth_login'), {'email': email, 'password': password})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {res.data['access']}')

    def test_get_all_cars(self):
        res = self.client.get(reverse('cars_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data
        self.assertEqual(len(data), 2)
        car1 = CarsModel.objects.get(pk=self.car1.pk)
        self.assertEqual(car1.brand, "BMW")
        car2 = CarsModel.objects.get(pk=self.car2.pk)
        self.assertEqual(car2.brand, "Audy")
        self.assertEqual(CarsModel.objects.count(), 2)

    def test_create_car_without_auth(self):
        sample_car = {
            "brand": "KIA",
            "price": 2000,
            "year": 2000,
            "body_type": "Jeep"
        }
        count_before = CarsModel.objects.count()
        res = self.client.post(reverse('cars_list_create'), sample_car)
        count_after = CarsModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(count_before, count_after)

    def test_create_car_with_auth(self):
        self._authenticate()
        sample_car = {
            "brand": "KIA",
            "price": 2000,
            "year": 2000,
            "body_type": "Jeep"
        }
        count_before = CarsModel.objects.count()
        res = self.client.post(reverse('cars_list_create'), sample_car)
        count_after = CarsModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_after, count_before +1)