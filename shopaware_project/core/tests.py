from rest_framework import status
from rest_framework.test import APIClient
from shopaware_project.tests import BaseTestCase


class PlacesTest(BaseTestCase):

    def test_get_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_places_endpoint(self):
        response = self.client.get('/places/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_place(self):
        data = {
            'name': 'a new place',
            'description': 'a new place description',
            'website': 'place@shopaware.com',
            'is_active': True
        }
        response = self.client.post('/places/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_place(self):
        data = {
            'name': 'a new place',
            'description': 'a new place description',
            'website': 'place@shopaware.com',
            'is_active': True
        }
        update_data = {
            'name': 'an updated place',
            'description': 'an updated place description',
            'website': 'updated_place@shopaware.com',
            'is_active': True
        }

        # Check that PUT succeeded and new item wasn't created
        post_response = self.client.post('/places/', data)
        update_response = self.client.put(post_response.data['url'], update_data)
        post_pk = post_response.data['url'].split('/')[-2]
        update_pk = update_response.data['url'].split('/')[-2]
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(post_pk, update_pk)

        # Check that item was actually changed.
        response = self.client.get(post_response.data['url'])
        self.assertEqual(response.data['name'], update_data['name'])
