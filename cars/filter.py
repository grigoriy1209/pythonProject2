from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from cars.models import CarsModel


def car_filter(query:QueryDict):
    qs = CarsModel.objects.all()

    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case _:
                raise ValidationError(f"Filter {k} is not valid")
    return qs