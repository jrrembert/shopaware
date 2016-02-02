# encoding: utf-8
#
# ./manage.py create_user
#
#
import argparse
import getpass

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction


class Command(BaseCommand):
    help = "Creates a Showaware user."

    parser = argparse.ArgumentParser()

    def add_arguments(self, parser):
        parser.add_argument('--email', dest='email', help=''),
        parser.add_argument('--username', dest='username', help=''),
        parser.add_argument('--password', dest='password', help='')

    def handle(self, *args, **kwargs):
        email = kwargs.get('email') or input("Email: ")
        username = kwargs.get('username') or input("User Name: ")
        password = kwargs.get('password') or getpass.getpass("Password: ")

        with transaction.atomic():
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()

            self.stdout.write(self.style.SUCCESS("User created."))
