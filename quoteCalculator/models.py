from django.db import models

# Create your models here.
class Quote( models.Model ):
    address        = models.CharField( max_length=200 )
    monthlyRent    = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    unitNumber     = models.IntegerField( default=0 )
    vacancy        = models.IntegerField( default=0 )
    bedrooms       = models.IntegerField( default=0 )
    bathrooms      = models.IntegerField( default=0 )
    annualTotal    = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    marketing      = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    taxes          = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    insurance      = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    repairs        = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    administration = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    payroll        = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    utility        = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    management     = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )
    cap_rate       = models.DecimalField( default=0.0, max_digits=12, decimal_places=2 )

