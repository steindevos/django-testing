from django.test import TestCase
from .models import Contact

class TestModelst(TestCase):
    
    def test_new_contact_is_not_important(self):
        contact = Contact(name="Jane", email="jane@example.com", phone="0634503450")
        contact.save()
        
        self.assertFalse(contact.important)
        
    def test_can_create_important_contact(self):
        contact = Contact(name="Jane", email="jane@example.com", phone="0634503450", important=True)
        contact.save()
        
        self.assertTrue(contact.important)