# Importing the necessary library
from django.shortcuts import render


# A view function that returns the 'crop_yield_prediction.html' template
def crop_yield_prediction(request):
    # Render the template with the context and return an HTTPResponse
    return render(request, 'crop_yield_prediction.html')
