from django.shortcuts import render
from datetime import datetime, timedelta

CROPS = ['Soyabeans', 'apple', 'beans', 'grapes', 'maize', 'peas', 'rice']


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
    if crop == 'Soyabeans':
        schedule.append({'date': start_date + timedelta(days=1), 'text': 'Irrigate for 30 minutes'})
        schedule.append({'date': start_date + timedelta(days=5), 'text': 'Irrigate for 1 hour'})
        schedule.append({'date': start_date + timedelta(days=15), 'text': 'Irrigate for 2 hours'})
    elif crop == 'apple':
        schedule.append({'date': start_date + timedelta(days=2), 'text': 'Irrigate for 1 hour'})
        schedule.append({'date': start_date + timedelta(days=7), 'text': 'Irrigate for 2 hours'})
        schedule.append({'date': start_date + timedelta(days=14), 'text': 'Irrigate for 2.5 hours'})
        schedule.append({'date': start_date + timedelta(days=28), 'text': 'Irrigate for 4 hours'})
    elif crop == 'beans':
        schedule.append({'date': start_date + timedelta(days=3), 'text': 'Irrigate for 45 minutes'})
        schedule.append({'date': start_date + timedelta(days=7), 'text': 'Irrigate for 1 hour'})
        schedule.append({'date': start_date + timedelta(days=12), 'text': 'Irrigate for 2 hours'})
    elif crop == 'grapes':
        schedule.append({'date': start_date + timedelta(days=1), 'text': 'Irrigate for 30 minutes'})
        schedule.append({'date': start_date + timedelta(days=6), 'text': 'Irrigate for 1 hour'})
        schedule.append({'date': start_date + timedelta(days=12), 'text': 'Irrigate for 2 hours'})
    elif crop == 'maize':
        schedule.append({'date': start_date + timedelta(days=1), 'text': 'Irrigate for 1 hour'})
        schedule.append({'date': start_date + timedelta(days=7), 'text': 'Irrigate for 2 hours'})
        schedule.append({'date': start_date + timedelta(days=14), 'text': 'Irrigate for 3 hours'})
        schedule.append({'date': start_date + timedelta(days=28), 'text': 'Irrigate for 4.5 hours'})

    elif crop == 'peas':
        schedule.append({'date': start_date + timedelta(days=1), 'text': 'Irrigate for 30 minutes'})
        schedule.append({'date': start_date + timedelta(days=4), 'text': 'Irrigate for 1 hour'})

        # Add more entries to the schedule for peas
        for i in range(7, 91, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate for 30 minutes'})

    elif crop == 'rice':
        schedule.append({'date': start_date + timedelta(days=3), 'text': 'Irrigate for 1 hour'})
        schedule.append({'date': start_date + timedelta(days=7), 'text': 'Irrigate for 2 hours'})
        schedule.append({'date': start_date + timedelta(days=14), 'text': 'Irrigate for 3 hours'})
        schedule.append({'date': start_date + timedelta(days=21), 'text': 'Irrigate for 4 hours'})

        # Add more entries to the schedule for rice
        for i in range(28, 151, 7):
            schedule.append({'date': start_date + timedelta(days=i), 'text': 'Irrigate for 1 hour'})

        # Format dates in the schedule to display the full month name and day number
        for entry in schedule:
            entry['date'] = entry['date'].strftime('%d %B %Y')
    return schedule
