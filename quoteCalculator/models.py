from django.db import models

# Create your models here.
class Quote( models.Model ):
	address = models.CharField( max_length=200 )
	cap_rate = models.DecimalField( max_digits=6, decimal_places=2 )