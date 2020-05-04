from django.test import TestCase
from django.contrib.auth import get_user_model


payload = {
    'email': 'test@mail.com',
    'password': "testpass",
}


def sample_user(email, password=None):
    return get_user_model().objects.create_user(email=email, password=password)


class UserModelTest(TestCase):
    """Common user model features"""

    def test_create_user(self):
        """Basic user creation"""

        user = sample_user(
            payload['email'],
            payload['password']
        )

        user_received = get_user_model().objects.get(email=payload['email'])

        self.assertEqual(user.id, user_received.id)
        self.assertTrue(user.email, payload['email'])
        self.assertTrue(user.check_password(payload['password']))

    def test_create_superuser(self):
        """Super user creation"""
        super_payload = {
            'email': 'super@mail.com',
            'password': 'superpuper',
        }

        stuff = get_user_model().objects.create_superuser(**super_payload)
        stuff_received = get_user_model().objects.get(email=super_payload['email'])

        self.assertEqual(stuff.id, stuff_received.id)
        self.assertEqual(stuff.email, super_payload['email'])
        self.assertEqual(stuff.is_staff, True)
        self.assertEqual(stuff.is_superuser, True)

    def test_user_reset_password(self):
        """Check checks if password can be changed"""

        user = sample_user(
            payload['email'],
            payload['password']
        )

        new_password = 'newtestpassword'
        user.set_password(new_password)

        self.assertTrue(user.check_password(new_password))

    def test_user_creation_with_normalize_email(self):
        """
        Is it normalize email working or not?
        """
        weird_email = 'test@MaIL.Com'
        user = sample_user(
            weird_email,
            payload['password']
        )

        self.assertEqual(user.email, 'test@mail.com')

    def test_raise_error_without_email(self):

        with self.assertRaises(ValueError):
            sample_user(None, 'password123!')
