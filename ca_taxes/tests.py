from decimal import Decimal
from django.core.management import call_command
from django.test import TestCase
from ca_taxes.models import CATax, CATaxManager


class CATaxesTestCase(TestCase):
    test_city = 'Test City'
    test_county = 'Test County'
    test_tax_rate = Decimal(0.10)  # 10% for Test City in Test County

    def setUp(self):
        tax = CATax.objects.create(city=self.test_city, rate=self.test_tax_rate, county=self.test_county)

    def test_ca_tax(self):
        taxes = CATax.objects.filter(city=self.test_city, county=self.test_county)
        self.assertEqual(1, len(taxes))

        rate = CATaxManager.lookup_tax_rate(self.test_city, self.test_county)
        self.assertAlmostEqual(self.test_tax_rate, rate)

    def test_wrong_situation(self):
        with self.assertRaises(ValueError):
            CATax.objects.create(city=self.test_city, rate=Decimal(0.20), county=self.test_county)
            CATaxManager.lookup_tax_rate(self.test_city, self.test_county)

    def test_not_ca_tax(self):
        self.assertAlmostEqual(CATaxManager.NO_TAX, CATaxManager.lookup_tax_rate('Some City', 'Some County', 'WA'))

    def test_ca_tax_import(self):
        CATax.objects.all().delete()
        call_command('cataxes')
        self.assertGreater(CATax.objects.count(), 0)
