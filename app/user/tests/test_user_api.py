from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse('user:create')
RETRIEVE_URL = reverse('user:update')
LIST_URL = reverse('user:list')
TOKEN_URL = reverse('user:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserAPITests(TestCase):

    payload = {
            'email': 'test@mail.com',
            'password': 'password231',
    }

    def setUp(self) -> None:
        self.client = APIClient()

    def get_token(self, payload):
        create_user(**payload)
        token = self.client.post(TOKEN_URL, payload)

        return token.data['token']

    def test_create_simple_user(self):
        """
        This test check a user creation
        """
        payload = {
            'email': 'test@mail.com',
            'password': 'password231',
            'name': 'vasia'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        u = get_user_model().objects.get(**res.data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(u.check_password(self.payload['password']))
        self.assertEqual(u.email, self.payload['email'])

    def test_user_already_exist(self):
        create_user(**self.payload)
        res = self.client.post(CREATE_USER_URL, self.payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_user_with_short_password_does_not_exist(self):
        payload = {'email': 'testtest@mail.com', 'password': 'pw'}

        self.client.post(CREATE_USER_URL, payload)
        user_not_exist = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_not_exist)

    def test_token_success_with_valid_credentials(self):

        create_user(**self.payload)

        token = self.client.post(TOKEN_URL, self.payload)

        self.assertEqual(token.status_code, status.HTTP_200_OK)
        self.assertContains(token, 'token')

    def test_get_token_with_invalid_password(self):
        """
        Check that response does not have token with invalid credentials
        """
        payload = {'email': 'test123@mail.com', 'password': ''}

        create_user(**payload)
        token = self.client.post(TOKEN_URL, payload)

        self.assertEqual(token.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_token_with_invalid_email(self):
        """
        Check that response does not have token with invalid credentials
        """
        payload = {'email': 'test123@mail.com', 'password': 'password231'}
        create_user(**payload)

        invalid_credentials = {'email': 'test124@mail.com', 'password': 'password231'}
        token = self.client.post(TOKEN_URL, invalid_credentials)

        self.assertEqual(token.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_use_token(self):
        payload = {'email': 'test123@mail.com', 'password': 'password231'}

        token = self.get_token(payload)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        res = self.client.get(RETRIEVE_URL)

        self.assertEqual(res.data['email'], payload['email'])
        self.assertNotIn('token', res.data)
        self.assertNotIn(payload['password'], res.data)

    def test_get_and_update_user_data(self):
        payload = {'email': 'test123@mail.com', 'password': 'password231'}

        token = self.get_token(payload)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        res = self.client.get(RETRIEVE_URL)

        new_payload = {
            'email': 'newtest@mail.com',
            'password': 'newpass123', 'name': 'vasia'
        }

        updated_user = self.client.patch(RETRIEVE_URL, new_payload)

        self.assertNotEqual(res.data['email'], updated_user.data['email'])
        self.assertNotContains(updated_user, 'password')
        self.assertNotContains(updated_user, token)

        u = get_user_model().objects.filter(email='newtest@mail.com').exists()
        self.assertTrue(u)
