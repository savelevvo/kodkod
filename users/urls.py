from .views import AuthUserRegister, AuthUserLogout, AuthUserLogin, AuthUserProfile
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
    path('login/', AuthUserLogin.as_view()),
    path('register/', AuthUserRegister.as_view()),
    path('logout/', AuthUserLogout.as_view()),
    path('<int:pk>/', AuthUserProfile.as_view()),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)
