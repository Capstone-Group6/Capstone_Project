from django.shortcuts import render
from datetime import datetime, timedelta

CROPS = ['Soybeans', 'Apple', 'Beans', 'Grapes', 'Maize', 'Peas', 'Rice']


def irrigation_planning(request):
    selected_crop = None
    selected_date = None
    irrigation_schedule = None

    if request.method == 'POST':
        selected_crop = request.POST['crop']
        selected_date = datetime.strptime(request.POST['plantation_date'], '%Y-%m-%d').date()
        irrigation_schedule = get_irrigation_schedule(selected_crop, selected_date)

    context = {
        'crops': CROPS,
        'selected_crop': selected_crop,
        'selected_date': selected_date,
        'irrigation_schedule': irrigation_schedule,
    }
    return render(request, 'irrigation_planning.html', context)


def get_irrigation_schedule(crop, date):
    schedule = []
    start_date = date
    # Add the irrigation schedule for the selected crop based on the plantation date
    if crop == 'Soybeans':
        schedule.append({'date': start_date + timedelta(days=4), 'text': 'Irrigate with 10-15mm water'})
        for i in range(12, 30, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30mm water'})
        for i in range(37, 60, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 40-45mm water'})
        for i in range(67, 80, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30mm water'})
    elif crop == 'Apple':
        schedule.append({'date': start_date + timedelta(days=0), 'text': 'Irrigate 5-10 liters per tree'})
        for i in range(7, 30, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30 liters per tree'})
        for i in range(37, 55, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 40-45 liters per tree'})
        schedule.append({'date': start_date + timedelta(days=0), 'text': 'Irrigate 25-30 liters thereafter'})

    elif crop == 'Beans':
        schedule.append({'date': start_date + timedelta(days=4), 'text': 'Irrigate with 10-15mm water'})
        for i in range(12, 30, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30mm water'})
        for i in range(37, 60, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 40-45mm water'})
        for i in range(67, 80, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30mm water'})
    elif crop == 'Grapes':
        schedule.append({'date': start_date + timedelta(days=0), 'text': 'Irrigate 20-25 liters per vine'})
        for i in range(7, 30, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 50-60 liters per vine'})
        for i in range(37, 55, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 100-120 liters per vine'})
        schedule.append({'date': start_date + timedelta(days=0), 'text': 'Irrigate 60-80 liters thereafter'})
    elif crop == 'Maize':
        schedule.append({'date': start_date + timedelta(days=4), 'text': 'Irrigate with 10-15mm water'})
        for i in range(12, 30, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30mm water'})
        for i in range(37, 60, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 40-45mm water'})
        for i in range(67, 80, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 60-80mm water'})

    elif crop == 'Peas':
        schedule.append({'date': start_date + timedelta(days=4), 'text': 'Irrigate with 10-15mm water'})
        for i in range(12, 30, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30mm water'})
        for i in range(37, 60, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 40-45mm water'})
        for i in range(67, 80, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate with 25-30mm water'})

    elif crop == 'Rice':
        schedule.append({'date': start_date + timedelta(days=0), 'text': 'Maintain the soil moist for proper '
                                                                         'germination'})
        schedule.append({'date': start_date + timedelta(days=14), 'text': 'Flood the field to a depth of '
                                                                          'approximately 5-10 cm for next 40 days'})
        schedule.append({'date': start_date + timedelta(days=40), 'text': 'Flood the field to a depth of '
                                                                          'approximately 10-15 cm for next 40 days'})
        schedule.append({'date': start_date + timedelta(days=40), 'text': 'Flood the field to a depth of '
                                                                          'approximately 5-10 cm for next 20 days'})
        schedule.append({'date': start_date + timedelta(days=20), 'text': 'Drain the field to allow the soil to dry '
                                                                          'before harvest'})

        # Format dates in the schedule to display the full month name and day number
        for entry in schedule:
            entry['date'] = entry['date'].strftime('%d %B %Y')
    return schedule
