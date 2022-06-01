from django.shortcuts import render
from django.views.generic import DetailView

from curatorapp.models import Permanent

# Create your views here.
class PermanentDetailView(DetailView):
    model = Permanent
    context_object_name = 'target_permanent'
    template_name = 'curatorapp/permanent_detail.html'