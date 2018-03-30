from django import forms
from .models import Quote

class CreateQuote( forms.ModelForm ):
	class Meta:
		model = Quote
		fields = [ 'address', 
		           'monthlyRent', 
		           'unitNumber',
		           'vacancy',
		           'bedrooms',
		           'bathrooms',
		           'annualTotal',
		           'marketing',
		           'taxes',
		           'insurance',
		           'repairs',
		           'administration',
		           'payroll',
		           'utility',
		           'management',
		           'cap_rate'
		          ]