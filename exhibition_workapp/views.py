from django.shortcuts import render
from django.views.generic import DetailView

from exhibition_workapp.models import Exhibition_work

# Create your views here.
class Exhibition_workDetailView(DetailView):
    model = Exhibition_work
    context_object_name = 'target_exhibition_work'
    template_name = 'exhibition_workapp/detail.html'