from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mail.com',
            password='testpassword1123!'
        )

        self.user = get_user_model().objects.create_user(
            email='test@mail.com',
            password='testpass234!'
        )

        self.client.force_login(self.admin_user)

    def test_user_changelist(self):

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.email)

    def test_user_add(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

