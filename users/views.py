from .forms import RegisterForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import AuthUser
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import AuthUserSerializer


class UserProfile(APIView):
    def get(self, request, pk, format=None):
        user = get_object_or_404(AuthUser, pk=pk)
        serializer = AuthUserSerializer(user)
        return Response(serializer.data)


def index(request):
    return render(request, 'index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@csrf_protect
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()

    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})


class UserLogin(APIView):
    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Someone tried to login and failed.")
            return HttpResponse("Invalid login details given")
