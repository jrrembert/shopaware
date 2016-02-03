from django.test import TestCase
from selenium import webdriver




class APISmokeTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()



    def tearDown(self):
        self.browser.quit()


    def root_url_loads(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django REST framework', self.browser.title)
