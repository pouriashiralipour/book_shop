from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class SignUpTest(TestCase):
    username = 'my_username'
    email = 'myusername@gmail.com'

    def test_signup_page_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)

    def test_signup_page_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEquals(response.status_code, 200)

    def test_signup_page_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEquals(get_user_model().objects.all().count(), 1)
        self.assertEquals(get_user_model().objects.all()[0].username, self.username)
        self.assertEquals(get_user_model().objects.all()[0].email, self.email)
