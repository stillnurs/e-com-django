from rest_framework.test import APITestCase
from authentication.models import User

from faker import Faker

faker = Faker()
password = faker.paragraph(nb_sentences=6)
fake_user = {
        'username': faker.name().split(' ')[0],
        'email': faker.email(),
        'password': password
        }



class TestModel(APITestCase):


    def test_creates_user(self):
        user = User.objects.create_user(fake_user['username'], fake_user['email'],fake_user['password'])
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, fake_user['email'])

    def test_creates_super_user(self):
        user = User.objects.create_superuser('George', 'gwashington@gmail.com', 'gw123456')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'gwashington@gmail.com')


    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='gwashington@gmail.com', password='gw123456')


    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='gwashington@gmail.com', password='gw123456')


    def test_raises_error_when_no_email_is_supplied(self):
            self.assertRaises(ValueError, User.objects.create_user, username='George', email='', password='gw123456')


    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='George', email='', password='gw123456')


    def test_cant_create_super_user_with_is_staff_status(self):
            with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
                User.objects.create_superuser(username='George', email='gwashington@gmail.com', password='gw123456', is_staff=False)
    
    
    def test_cant_create_super_user_with_super_user_status(self):
                with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
                    User.objects.create_superuser(username='George', email='gwashington@gmail.com', password='gw123456', is_superuser=False)



