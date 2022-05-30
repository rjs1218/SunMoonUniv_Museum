from django.urls import path

from siteapp.views import IntroductionHistoryView, MainView

app_name = "siteapp"

urlpatterns = [
    path('history/', IntroductionHistoryView, name='history'),
    path('main/', MainView, name='main'),
]