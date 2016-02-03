from rest_framework.test import APIClient
from shopaware_project.tests import BaseTestCase


class PlacesTest(BaseTestCase):

    client = APIClient(username=BaseTestCase.USERNAME,
                       password=BaseTestCase.PASSWORD,
                       email=BaseTestCase.EMAIL)

    def test_create_place(self):
        response = self.client.post('/places/', {'name': 'test'})
        self.assertEqual(response.status_code, 200)
