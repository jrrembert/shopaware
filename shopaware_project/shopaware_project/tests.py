from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class BaseTestCase(TestCase):

    USERNAME = 'test'
    PASSWORD = 'testtest'
    EMAIL = 'test@test.com'

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.client = APIClient()
        self.user = User.objects.create_user(
                        self.USERNAME,
                        self.EMAIL,
                        self.PASSWORD)
        self.client.login(username=self.USERNAME,
                          password=self.PASSWORD)

    def tearDown(self):
        self.client.logout()
        self.user.delete()
