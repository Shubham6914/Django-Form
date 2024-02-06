# models.py

from django.db import models

class Registration(models.Model):
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    business = models.CharField(max_length=255)
    employees = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    additional = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    place = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    your_email = models.EmailField()
    accept_terms = models.BooleanField(default=False)
