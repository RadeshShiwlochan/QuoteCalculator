from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote
from .forms import CreateQuote

# Create your views here.
from .models import Quote

def home( request ):
	quotes = Quote.objects
	return render( request, 'quoteCalculator/home.html' , { 'quotes': quotes } )

def calculateQuote( request ):
    return render( request, 'quoteCalculator/calculateQuote.html' )	

def calculate_rate( request ):
    form = CreateQuote(request.POST or None )

    if form.is_valid():
        form.save()
        return render( request, 'quoteCalculator/result.html' )
    return render( request, 'quoteCalculator/calculateQuote.html' )    
