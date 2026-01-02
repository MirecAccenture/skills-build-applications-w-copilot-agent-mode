from rest_framework.test import APITestCase


class AuthAPITest(APITestCase):
    def test_registration_login_and_me(self):
        reg_url = '/api/auth/registration/'
        login_url = '/api/auth/login/'
        me_url = '/api/users/me/'

        # Register a new user
        reg_data = {
            'username': 'tester',
            'email': 'tester@example.com',
            'password1': 'strong-password-123',
            'password2': 'strong-password-123',
        }
        r = self.client.post(reg_url, reg_data)
        self.assertIn(r.status_code, (200, 201))

        # Log in to obtain token
        login_data = {'username': 'tester', 'password': 'strong-password-123'}
        r = self.client.post(login_url, login_data)
        self.assertEqual(r.status_code, 200)
        token = r.data.get('key') or r.data.get('token')
        self.assertIsNotNone(token)

        # Access protected endpoint with token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        r = self.client.get(me_url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data.get('username'), 'tester')
