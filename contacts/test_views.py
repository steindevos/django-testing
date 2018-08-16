from django.test import TestCase

#create your tests here
class TestViews(TestCase): 
    def test_root_url(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)