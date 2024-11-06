from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class StatusCodeTestCase(APITestCase):
    def test_create_account(self):
        url = reverse('topic-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


