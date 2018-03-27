from django.shortcuts import render

# Create your views here.
from .models import Quote

def home( request ):
	quotes = Quote.objects
	return render( request, 'quoteCalculator/home.html' , { 'quotes': quotes } )
