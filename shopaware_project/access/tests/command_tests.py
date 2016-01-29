from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase

from shopaware_project.tests import BaseTestCase


class TestCustomCommands(BaseTestCase):

    email = 'talib@kweli.com'
    username = 'blackstar'
    password = 'blackstar'

    def test_create_user(self):
        """Test that the `create_user` custom manage.py command creates a
           user with the specified email, username, and password.
        """
        call_command('create_user', email=self.email, username=self.username,
            password=self.password)
        user = User.objects.get(username=self.username)
        self.assertEquals(user.email, 'talib@kweli.com')
