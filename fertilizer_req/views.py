from django.shortcuts import render


# Define a view function called `fertilizer_requirement`
def fertilizer_requirement(request):
    # Render the `fertilizer_requirement.html` template and return the resulting HTTP response
    return render(request, 'fertilizer_requirement.html')
