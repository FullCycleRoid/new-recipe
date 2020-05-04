from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag, Ingredient


TAG_CREATE_URL = reverse('recipe:tag-create')
TAG_LIST_URL = reverse('recipe:tag-list')
TOKEN_URL = reverse('user:token')
TAG_RETRIEVE_URL = reverse('recipe:detail', kwargs={'name': 'Banana'})

INGREDIENTS_URL = reverse('recipe:ingredients-list')
INGREDIENT_URL = reverse('recipe:ingredients-detail', kwargs={'pk': '1'})


def sample_user_create(**params):
    return get_user_model().objects.create_user(**params)


def get_token(**user_data):
    client = APIClient()
    token = client.post(TOKEN_URL, user_data)
    return token.data['token']


class TagTestCase(TestCase):
    user_data = {
        'email': 'testtest@mail.com',
        'password': 'pass123'
    }

    def setUp(self) -> None:
        self.client = APIClient()
        self.unauthenticated_client = APIClient()

        self.user = sample_user_create(**self.user_data)
        self.token = get_token(**self.user_data)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

        self.tag1 = Tag.objects.create(name='Banana', user=self.user)
        self.ingredient = Ingredient.objects.create(name='Sugar', user=self.user)

    def test_create_tag_by_authenticated_user_success(self):
        """
        Check only authenticated user can create tag object
        """

        res = self.client.post(TAG_CREATE_URL, {'name': 'Apple', 'user': self.user.id})

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], 'Apple')

    def test_create_tag_by_unauthenticated_user_fail(self):
        """
        Unauthenticated used cannot create tag
        """
        res = self.unauthenticated_client.post(TAG_CREATE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_tag_list_allow_any(self):
        """
        Check is the Tag list available for AnonymousUser
        """
        Tag.objects.create(name='Melon', user=self.user)
        res = self.client.get(TAG_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue((len(res.data) > 0))

    def test_tag_retrieve_success(self):
        """
        Check the tag retrieve available for object owner only
        """
        res = self.client.get(TAG_RETRIEVE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], 'Banana')

    def test_tag_update_success(self):
        """
        Check the tag update available for object owner only
        """
        res = self.client.put(TAG_RETRIEVE_URL, {'name': 'Celery', 'user': self.user.id})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # def test_tag_update_available_for_owner_only(self):
    #     """
    #     It is not owner can't update the tag
    #     """
    #     client = APIClient()
    #
    #     not_owner_data = {
    #         'email': 'notowner@mail.com',
    #         'password': 'testpass'
    #     }
    #
    #     wrong_user = sample_user_create(**not_owner_data)
    #
    #     token = get_token(**not_owner_data)
    #     client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    #     res = client.put(TAG_RETRIEVE_URL, {'name':'wrong', 'user': wrong_user.id})
    #
    #     self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    # def test_tag_CRUD_delete_success(self):
    #     """
    #     Check the tag delete is success
    #     """
    #
    #
    def test_tag_update_unavailable_for_unauthenticated_user(self):
        """
        Check the tag update unavailable for unauthenticated user
        """


    def test_ingredients_CRUD_delete_success(self):
        """
        Check the tag object delete success
        """
        print(reverse('recipe:ingredients-detail', kwargs={'pk': self.ingredient.pk}))
        res = self.client.delete(reverse('recipe:ingredients-detail', kwargs={'pk': self.ingredient.pk}))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


    def test_ingredients_CRUD_delete_available_for_owner_only(self):
        """
        Check is the tag object delete available only for object owner
        """


    def test_ingredients_create_success(self):
        """
        Check the tag object create success
        """


    def test_ingredients_list(self):
        """
        Check the tag object list success
        """


    def test_ingredients_update_success(self):
        """
        Check the tag object update success
        """

    def test_tag_delete(self):

        res = self.client.delete(TAG_RETRIEVE_URL)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)