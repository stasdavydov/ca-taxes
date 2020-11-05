from django.core.management import BaseCommand, CommandError
import requests
from ca_taxes.models import CATax


class Command(BaseCommand):
    CA_TAX_TABLE = 'http://www.boe.ca.gov/sutax/files/city_rates.csv'

    def handle(self, *args, **options):
        self.stdout.write('Import CA taxes from {0}...'.format(self.CA_TAX_TABLE))

        r = requests.get(self.CA_TAX_TABLE)
        if r.status_code != 200:
            raise CommandError('Cannot get content of ' + self.CA_TAX_TABLE)

        inserted, updated = CATax.objects.import_csv(r.text)

        self.stdout.write('Successfully imported CA taxes from {0}, new: {1}, updated: {2}'.format(
            self.CA_TAX_TABLE, inserted, updated))


