from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Quote

def home( request ):
	quotes = Quote.objects
	return render( request, 'quoteCalculator/home.html' , { 'quotes': quotes } )

def calculateQuote( request ):
    return render( request, 'quoteCalculator/calculateQuote.html' )	

def calculate_rate( request ):
    first_name = request.GET['firstname']
    last_name  = request.GET['lastname']
    user_name  = request.GET['username']
    email      = request.GET['email']
    address    = request.GET['address']
    print('This is the first and last name')
    print( first_name)
    print( last_name)
    print( user_name )
    print( email )
    print( address )
    return render( request, 'quoteCalculator/result.html' )    
