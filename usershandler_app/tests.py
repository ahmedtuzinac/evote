from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your tests here.


class RegisterTest(APITestCase):

    def test_register(self):
        data = {
            "username":"testusername",
            "password":"testpassword",
            "name":"Ahmed Tuzinac",
            "uniquenumber":"1807001783941"
        }

        url = reverse("register")
        response = self.client.post(url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class LoginLogoutTest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testusername",
            password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
    def test_login(self):

        data = {
            "username":"testusername",
            "password":"testpassword"
        }
        url = reverse("login")
        response = self.client.post(url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

