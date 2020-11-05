# California Taxes Django App

Django based app provides an easy way to get tax rate for city and county in California, US.
It provides Data Model `CATax` and management command for extracting state data.

## Installation

Install `ca-taxes`:

```
pip install ca-taxes
```

Add `ca-taxes` to `INSTALLED_APPS` in Django settings:

```
INSTALLED_APPS = (
  # ...
  'ca_taxes',
  # ...
)
```

Run Django migrations:
```
python manage.py migrate
```

Import CA taxes data from [California State Board of Equalization](http://www.boe.ca.gov/).
```
python manage.py cataxes
```

## Usage

```
CATaxManager.lookup_tax_rate('Los Angeles', self.test_county)
```
