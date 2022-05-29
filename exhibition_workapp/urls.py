from django.urls import path

from exhibition_workapp.views import Exhibition_workDetailView

app_name = "exhibition_workapp"

urlpatterns = [
    path('detail/<int:pk>', Exhibition_workDetailView.as_view(), name='detail'),
]