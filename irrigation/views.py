from django.shortcuts import render


# Render the irrigation_planning.html template
def irrigation_planning(request):
    return render(request, 'irrigation_planning.html')