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