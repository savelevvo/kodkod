import string

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from factory import DjangoModelFactory
from factory.fuzzy import FuzzyText

from .models import AuthUser


class UserFactory(DjangoModelFactory):
    username = FuzzyText(chars=string.ascii_lowercase)
    password = FuzzyText(length=10)

    class Meta:
        model = AuthUser


class AuthUserTests(APITestCase):
    def test_register(self):
        credentials = {
            'username': FuzzyText(chars=string.ascii_lowercase),
            'password': FuzzyText(length=12)
        }
        response = self.client.post(reverse('authuser-register'), credentials)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_existing(self):
        user = UserFactory()
        credentials = {
            'username': user.username,
            'password': user.password
        }
        response = self.client.post(reverse('authuser-register'), credentials)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
