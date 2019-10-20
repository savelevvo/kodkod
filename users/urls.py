from django.conf.urls import url
from .views import register, UserLogin, UserProfile
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^user_profile/$', UserProfile.as_view(), name='user_profile'),
    # url(r'^user_login/$', user_login, name='user_login'),
    path('login/', UserLogin.as_view()),
    path('<int:pk>/', UserProfile.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
