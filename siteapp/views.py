from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from siteapp.models import Introduction_history


# Create your views here.
def IntroductionHistoryView(request):
    history = Introduction_history.objects
    template = loader.get_template('siteapp/history.html')
    context = {
        'history': history,
    }
    return HttpResponse(template.render(context, request))

def MainView(request):
    return render(request, 'siteapp/main.html')

def HelloView(request):
    return render(request, 'siteapp/hello.html')

def GroupView(request):
    return render(request, 'siteapp/group.html')

def GuideFacilityView(request):
    return render(request, 'siteapp/guide_facility.html')

def GuideDonationView(request):
    return render(request, 'siteapp/guide_donation.html')