from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Poll


class PollsList(ListView):
    model = Poll


class PollDetail(DetailView):
    model = Poll
    pk_url_kwarg = 'id'
