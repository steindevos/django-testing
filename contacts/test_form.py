from django.test import TestCase
from .forms import ContactForm
# Create your tests here.


class TestContactForm(TestCase):
    def test_form_is_valid(self):  #test has to start with 'test_'
        form = ContactForm({
            "name": 'HankyPanky',
            "email": 'hankypanky@example.com',
            "phone": '06123456789',
        })
        
        self.assertTrue(form.is_valid())
        
    def test_name_is_required(self):
        form = ContactForm({
            "email": "test@example.com",
            "phone": "065134234"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_email_is_required(self):
        form = ContactForm({
            "name": "test",
            "phone": "065134234"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_phone_is_required(self):
        form = ContactForm({
            "name": "test",
            "email": "065134234"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_valid_email(self):
        form = ContactForm({
            "name": "Peter",
            "email": "ssldkfjsld",
            "phone": "040430"
        })
        
        self.assertFalse(form.is_valid())