from django.contrib import admin
from django.urls import path
from rest_framework import routers

from users.views import AuthUserView
from polls.views import PollView

router = routers.SimpleRouter()
router.register(r'users', AuthUserView)
router.register(r'polls', PollView)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
