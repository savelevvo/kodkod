from .views import PollsList, PollDetail, UserPolls
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', PollsList.as_view()),
    path('<int:pk>/', PollDetail.as_view()),
    path('user/<int:pk>/', UserPolls.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
