from django.urls import path

from siteapp.views import GroupView, IntroductionHistoryView, MainView, HelloView

app_name = "siteapp"

urlpatterns = [
    path('history/', IntroductionHistoryView, name='history'),
    path('main/', MainView, name='main'),
    path('hello/', HelloView, name='hello'),
    path('group/', GroupView, name='group'),
]