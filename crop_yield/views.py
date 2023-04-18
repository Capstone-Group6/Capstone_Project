from django.shortcuts import render

# Define the yield per hectare for each crop
CROP_YIELDS = {
    'Apple': 19860,
    'Beans': 1891,
    'Grapes': 1330,
    'Maize': 9263,
    'Peas': 2291,
    'Rice': 3000,
    'Soybeans': 3039,
}


def crop_yield_prediction(request):
    if request.method == 'POST':
        # Get the user's inputs from the form
        crop = request.POST.get('crop')
        area = float(request.POST.get('area'))

        # Calculate the predicted yield based on the crop and area
        if crop in CROP_YIELDS:
            yield_per_hectare = CROP_YIELDS[crop]
            predicted_yield = yield_per_hectare * area
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

