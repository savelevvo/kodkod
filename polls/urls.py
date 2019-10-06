from django.conf.urls import url
from .views import PollsList, PollDetail

urlpatterns = [
    url(r'^$', PollsList.as_view(), name='all_polls'),
    url(r'^(?P<id>[0-9]+)/$', PollDetail.as_view(), name='detail_poll'),
]
