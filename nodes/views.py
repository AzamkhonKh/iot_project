from operator import imod
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
# Create your views here.
from .models import Node
class IndexView(generic.ListView):
    context_object_name = 'latest_node_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Node.objects.order_by('-pub_date')[:5]
