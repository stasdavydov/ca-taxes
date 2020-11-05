from django.contrib import admin
from ca_taxes.models import CATax, CATaxManager


def percent(tax_rate):
    return '{0:.2f}%'.format(tax_rate.rate * CATaxManager.HUNDRED)
percent.short_description = u'Tax Rate'


class CATaxAdmin(admin.ModelAdmin):
    list_display = ('city', percent, 'county')
    search_fields = ['city', 'rate', 'county']
    list_filter = ('county', )

admin.site.register(CATax, CATaxAdmin)
