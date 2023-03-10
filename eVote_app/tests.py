from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from eVote_app.models import PoliticalElection




class PoliticalElectionTest(APITestCase):

    def testElectionList(self):
        url = reverse("elections-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    