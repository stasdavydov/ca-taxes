import csv
from decimal import Decimal
from io import StringIO

from django.db import models


class NotEnoughDataError(Exception):
    pass


class CATaxManager(models.Manager):
    CA = 'CA'
    NO_TAX = Decimal(0.00)
    DEFAULT_CA_TAX = Decimal(0.09)  # default 9% CA Tax for not found cities
    HUNDRED = Decimal(100.00)

    @staticmethod
    def lookup_tax_rate(city, county, state=CA):
        if state == CATaxManager.CA:
            taxes = CATax.objects.filter(city=city, county=county)
            if len(taxes) == 0:
                return CATaxManager.DEFAULT_CA_TAX
            elif len(taxes) == 1:
                return taxes[0].rate
            else:
                base_rate = taxes[0].rate
                for tax in taxes:
                    if tax.rate != base_rate:
                        raise ValueError('More than one tax area found with different tax rates')
                return base_rate
        elif not state or len(state) == 0:
            raise NotEnoughDataError('State is not specified')
        else:
            return CATaxManager.NO_TAX

    def import_csv(self, csv_text):
        f = StringIO(csv_text)
        reader = csv.reader(f, delimiter=',')
        actual_data = False

        def p2d(x):
            return Decimal(x.strip('%')) / self.HUNDRED

        def clean_city(city):
            return city.replace('*', '')

        inserted = 0
        updated = 0
        for row in reader:
            if not actual_data:
                actual_data = (row == ['City', 'Rate', 'County'])
            else:
                tax = CATax(city=clean_city(row[0]), rate=p2d(row[1]), county=row[2])
                try:
                    present = CATax.objects.get(city=tax.city, county=tax.county)
                    tax.id = present.id
                    tax.save()
                    updated += 1
                except CATax.DoesNotExist:
                    tax.save()
                    inserted += 1
        return inserted, updated


class CATax(models.Model):
    city = models.CharField(max_length=100, db_index=True)
    rate = models.DecimalField(decimal_places=4, max_digits=6)
    county = models.CharField(max_length=100, db_index=True)

    objects = CATaxManager()

    def __str__(self):
        return u'{0.city}, {0.county} {0.rate}'.format(self)

    class Meta:
        verbose_name = u'CA Tax'
        verbose_name_plural = u'CA Taxes'
        ordering = ['city']
