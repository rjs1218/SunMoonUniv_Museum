from django.urls import path

from siteapp.views import IntroductionHistoryView

app_name = "siteapp"

urlpatterns = [
    path('history/', IntroductionHistoryView, name='history'),
]