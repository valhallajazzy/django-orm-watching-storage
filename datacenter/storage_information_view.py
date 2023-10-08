from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visiters_now = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visiter in visiters_now:
        duration_seconds = Visit.get_duration(visiter)
        duration = Visit.format_duration(duration_seconds)
        form = {
            'who_entered': f'{visiter.passcard}',
            'entered_at': f'{localtime(visiter.entered_at).strftime("%Y-%m-%d  %H.%M")}',
            'duration': f'{duration}',
        }
        non_closed_visits.append(form)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
