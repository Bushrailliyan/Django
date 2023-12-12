from django.test import TestCase,Client
from django.urls import reverse,resolve
from shopping.models import Product
from django.contrib.auth.models import User
class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='testpass')

    def test_viewshome(self):
        client = Client()
        client.login(username='testuser',password='testpass')
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')

    # def test_viewscreate(self):
    #     client = Client()
    #     response = client.get(reverse('create'))
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response,'index.html')


