from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    important = models.BooleanField(default=False, null=False, blank=False)
    
    def __str__(self):
        return self.name
        
    