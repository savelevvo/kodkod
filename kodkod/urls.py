from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import AuthUserView
from polls.views import PollView

router = routers.SimpleRouter()
router.register(r'users', AuthUserView, base_name='authuser')
router.register(r'polls', PollView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls'))
] + router.urls
