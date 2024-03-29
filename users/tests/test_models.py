from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersManagersTests(TestCase):

    def test_create_user(self) -> None:
        user = User.objects.create_user(email='user@user.com', password='foo')
        self.assertEqual('user@user.com', user.email)
        self.assertEqual('user@user.com', str(user))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')

    def test_create_superuser(self) -> None:
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual('super@user.com', admin_user.email)
        self.assertEqual('super@user.com', str(admin_user))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', password='foo', is_staff=False)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', password='foo', is_superuser=False)

    def test_user_attr(self) -> None:
        user = User.objects.create_user(first_name='Bruce', last_name='Wayne', email='bruce@wayne.we', password='foo')
        self.assertEqual(f'{user.first_name} {user.last_name}', user.get_full_name)
        self.assertEqual(user.first_name, user.get_short_name)
