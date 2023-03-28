from django.shortcuts import render

# Define the yield per square meter for each crop
CROP_YIELDS = {
    'wheat': 2.5,
    'corn': 3.0,
    'soybeans': 2.0,
    'rice': 4.0,
    'potatoes': 5.0,
    'tomatoes': 6.0,
    'peppers': 7.0,
}


def crop_yield_prediction(request):
    if request.method == 'POST':
        # Get the user's inputs from the form
        crop = request.POST.get('crop')
        area = float(request.POST.get('area'))

        # Calculate the predicted yield based on the crop and area
        if crop in CROP_YIELDS:
            yield_per_sq_meter = CROP_YIELDS[crop]
            predicted_yield = yield_per_sq_meter * area
        else:
            predicted_yield = None

        # Render the same page with the results included
        return render(request, 'crop_yield_prediction.html', {
            'crops': CROP_YIELDS.keys(),
            'selected_crop': crop,
            'selected_area': area,
            'yield_prediction': predicted_yield,
        })
    else:
        # Render the initial form page
        return render(request, 'crop_yield_prediction.html', {
            'crops': CROP_YIELDS.keys(),
        })

