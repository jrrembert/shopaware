from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class BaseTestCase(TestCase):

    USERNAME = 'test'
    PASSWORD = 'testtest'
    EMAIL = 'test@test.com'

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.user = User.objects.create_user(
                        self.USERNAME,
                        self.EMAIL,
                        self.PASSWORD)

    def tearDown(self):
        self.user.delete()


class ShopawareTestClient(Client):

    def __init__(self, username=None, password=''):
        self.username = username
        self.password = password

    def login(self, username=None, password=None):
        if username:
            self.user = User.objects.get(username=username)
            self.password = password or self.password

    def logout():
        pass
