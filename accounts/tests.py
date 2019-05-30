from django.test import TestCase

from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse


class AccountTest(APITestCase):

    def setUp(self):
        self.testuser = User.objects.create_user(username='dwaaw',email='1',password='2')
        self.createurl = reverse('account_create')


    def test_create_user(self):
        data = {'username': "daada",
                'email': "dadmamdamd@mdawda.com",
                'password': "12345678",
                }
        response = self.client.post(self.createurl,data,format='json')

        self.assertEqual(User.objects.count(), 2)
