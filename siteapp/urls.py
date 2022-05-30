from django.urls import path

from siteapp.views import GroupView, GuideDonationView, GuideFacilityView, IntroductionHistoryView, MainView, HelloView

app_name = "siteapp"

urlpatterns = [
    path('history/', IntroductionHistoryView, name='history'),
    path('main/', MainView, name='main'),
    path('hello/', HelloView, name='hello'),
    path('group/', GroupView, name='group'),
    path('guide_facility/', GuideFacilityView, name='guide_facility'),
    path('guide_donation/', GuideDonationView, name='guide_donation'),
]