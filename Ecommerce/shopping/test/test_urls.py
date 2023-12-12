from django.test import SimpleTestCase
from django.urls import reverse,resolve
from shopping.views import home
from shopping.views import create

class TestUrl(SimpleTestCase):
    def test_home(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)

    def test_create(self):
        url = reverse('create')
        print(resolve(url))
        self.assertEquals(resolve(url).func,create)
