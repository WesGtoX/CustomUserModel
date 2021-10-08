from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserViewSetTests(APITestCase):

    def setUp(self):
        self.data = {'email': 'normal@user.com', 'password': 'foo'}

    def test_perform_create(self):
        response = self.client.post(reverse('user-list'), data=self.data)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.data, dict)

    def test_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve(self):
        response = self.client.get(reverse('user-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update(self):
        response = self.client.put(reverse('user-detail', args=[1], kwargs={}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update(self):
        response = self.client.patch(reverse('user-detail', args=[1], kwargs={}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_destroy(self):
        response = self.client.delete(reverse('user-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
