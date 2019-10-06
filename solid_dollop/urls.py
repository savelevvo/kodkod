from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^users/', include('users.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
