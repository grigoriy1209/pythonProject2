from django.db import models


class CarQuerySet(models.QuerySet):
    def less_then_year(self, year):
        return self.filter(year__lt=year)

    def only_lada(self):
        return self.filter(brand='lada')


class CarManager(models.Manager):
    def get_queryset(self):
        return CarQuerySet(self.model)

    def less_then_year(self, year):
        return self.get_queryset().less_then_year(year)

    def only_lada(self):
        return self.get_queryset().only_lada()