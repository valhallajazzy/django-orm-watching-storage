from .models import Passcard
from .models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits=[]
    for visit in visits:
        duration = visit.format_duration()
        is_strange = visit.is_visit_long()
        form = {
            'entered_at': localtime(visit.entered_at).strftime("%Y-%m-%d  %H.%M"),
            'duration': duration,
            'is_strange': is_strange
        }
        this_passcard_visits.append(form)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


def storage_information_view(request):
    visiters_now = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visiter in visiters_now:
        duration = visiter.format_duration()
        form = {
            'who_entered': visiter.passcard,
            'entered_at': localtime(visiter.entered_at).strftime("%Y-%m-%d  %H.%M"),
            'duration': duration,
        }
        non_closed_visits.append(form)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


def active_passcards_view(request):
    active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_passcards,
    }
    return render(request, 'active_passcards.html', context)