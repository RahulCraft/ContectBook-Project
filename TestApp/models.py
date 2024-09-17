from typing import Any
from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    
