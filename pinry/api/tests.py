from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class RecentPinsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/pin/?format=json'

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
