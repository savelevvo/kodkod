from django.test import TestCase
import requests


class QuestionModelTests(TestCase):

    def test_authuser_register(self):
        # Can't register with username that already exists
        # existing_name = 'admin'
        # r = requests.post('http://127.0.0.1:8000/users/register/',
        #                   data={'username': existing_name, 'password': ''})
        # self.assertEqual(r.status_code, 400)
        pass

    def test_authuser_login(self):
        # Logged in user can't log in or register again
        # r = requests.post('http://127.0.0.1:8000/users/login/',
        #                   data={'username': 'admin', 'password': 'admin'})
        #
        # token = r.json()['token']
        # headers = {'Authorization': f'Token {token}'}
        # r = requests.post('http://127.0.0.1:8000/users/login/',
        #                   data={'username': 'admin', 'password': 'admin'},
        #                   headers=headers)
        # self.assertEqual(r.status_code, 400)
        #
        # # Can't login with wrong or empty credentials
        # credentials = ({'username': '', 'password': ''},
        #                {'username': 'admin', 'password': ''},
        #                {'username': '', 'password': '123Qwerty'},
        #                {'username': ',zxcmvndjf', 'password': '13q16'})
        # for c in credentials:
        #     r = requests.post('http://127.0.0.1:8000/users/login/', data=c)
        #     self.assertEqual(r.status_code, 400)
        pass

    def test_authuser_logout(self):
        pass

    def test_authuser_profile(self):
        pass