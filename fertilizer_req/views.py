from django.shortcuts import render

# Define the fertilizer requirements for different crops
fertilizer_requirement = {
    "Apples": {"nitrogen": 100, "phosphorous": 30, "potassium": 125},
    "Beans": {"nitrogen": 60, "phosphorous": 45, "potassium": 45},
    "Grapes": {"nitrogen": 60, "phosphorous": 15, "potassium": 60},
    "Maize": {"nitrogen": 200, "phosphorous": 70, "potassium": 135},
    "Peas": {"nitrogen": 45, "phosphorous": 25, "potassium": 25},
    "Rice": {"nitrogen": 120, "phosphorous": 45, "potassium": 75},
    "Soybeans": {"nitrogen": 65, "phosphorous": 25, "potassium": 65},
}


def fertilizer_req(request):
    if request.method == "POST":
        crop = request.POST.get("crop")
        area = float(request.POST.get("area"))
        # Calculate the fertilizer requirements based on the selected crop and area
        nitrogen = area * fertilizer_requirement[crop]["nitrogen"]
        phosphorous = area * fertilizer_requirement[crop]["phosphorous"]
        potassium = area * fertilizer_requirement[crop]["potassium"]
        # Pass the fertilizer requirements to the template context
        context = {"crop": crop, "area": area, "nitrogen": nitrogen, "phosphorous": phosphorous, "potassium": potassium}
        # Add the list of available crops to the context
        crops = list(fertilizer_requirement.keys())
        context["crops"] = crops
        # Render the HTML template with the fertilizer requirements in the context
        return render(request, "fertilizer_requirement.html", context)
    else:
        # Return the list of available crops to select from
        crops = list(fertilizer_requirement.keys())
        return render(request, "fertilizer_requirement.html", {"crops": crops})
