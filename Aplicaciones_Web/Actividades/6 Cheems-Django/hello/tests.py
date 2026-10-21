from unittest.mock import patch

from django.test import RequestFactory, SimpleTestCase

from .entities.user import User
from .enums.profile import Profile
from . import views


class IndexViewTests(SimpleTestCase):
    def test_index_displays_users(self):
        users = [User("Ada Lovelace", "alovelace", Profile.ADMINISTRADOR)]

        with patch("hello.views.User.get_all", return_value=users):
            response = views.index(RequestFactory().get("/"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ada Lovelace")
        self.assertContains(response, "alovelace")
        self.assertContains(response, "Administrador")
