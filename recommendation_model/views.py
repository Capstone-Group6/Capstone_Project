# Import required libraries
from django.shortcuts import render
from joblib import load

# Load the pre-trained model
model = load('./savedModels/model.joblib')


# Define a view function for crop recommendation
def crop_recommend(request):
    # Check if request method is POST
    if request.method == 'POST':
        # Get input values from user
        n = request.POST['n']
        p = request.POST['p']
        k = request.POST['k']
        temp = request.POST['temp']
        humidity = request.POST['humidity']
        ph = request.POST['ph']
        rainfall = request.POST['rainfall']
        # Use the loaded model to predict the recommended crop
        y_pred = model.predict([[n, p, k, temp, humidity, ph, rainfall]])
        # Render the template with the predicted crop as result
        return render(request, 'crop_recommend.html', {'result': y_pred})
    # Render the empty form template for GET requests
    return render(request, 'crop_recommend.html')