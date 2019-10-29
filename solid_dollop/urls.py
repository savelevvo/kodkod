from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from users.views import AuthUserView

router = routers.SimpleRouter()
router.register(r'users', AuthUserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
] + router.urls
