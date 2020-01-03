import string

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from factory import DjangoModelFactory
from factory.fuzzy import FuzzyText

from .models import AuthUser
from django.utils.crypto import get_random_string


class UserFactory(DjangoModelFactory):
    username = FuzzyText(chars=string.ascii_lowercase)

    class Meta:
        model = AuthUser


class AuthUserTests(APITestCase):

    def test_register(self):
        username = get_random_string(12, string.ascii_lowercase + string.digits)
        password = get_random_string(12, string.ascii_lowercase + string.digits)
        credentials = {
            'username': username,
            'password': password
        }
        response = self.client.post(reverse('authuser-register'), credentials)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_existing(self):
        pass

    def test_token(self):
        pass

    def test_token_refresh(self):
        pass
