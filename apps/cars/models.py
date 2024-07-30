from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel


class CarsModel(BaseModel):

    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=10, validators=(V.MinLengthValidator(2), ))
    price = models.IntegerField(validators=(V.MinValueValidator(0), V.MaxValueValidator(1_000_000)))
    year = models.IntegerField(validators=(V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)))
