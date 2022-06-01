from django.urls import path

from curatorapp.views import PermanentDetailView

app_name = "curatorapp"

urlpatterns = [
    # 작품 리스트

    # 작품 설명
    path('permanent_detail/<int:pk>', PermanentDetailView.as_view(), name='permanent_detail'),
]