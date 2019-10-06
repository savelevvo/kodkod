from django.conf.urls import url
from .views import register, user_login, UserProfile

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^user_profile/$', UserProfile.as_view(), name='user_profile'),
    url(r'^user_login/$', user_login, name='user_login'),
]
