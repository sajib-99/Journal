from django.db import models

from django.contrib.auth.models import User

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

import random

def random_string():
    return str(random.randint(10000, 99999))



# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    tropic = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
          return "Message from: " + self.name + ' --  Tropic : ' + self.tropic


class Editor_Request(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=11)
    phone = models.CharField(max_length=11)
    cv = models.FileField(upload_to='Editor_Request/cv/')

    def __str__(self):
          return "Joining Request from: " + self.First_Name + '  ' + self.Last_Name

class Reviewer_Request(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=11)
    phone = models.CharField(max_length=11)
    cv = models.FileField(upload_to='Reviewer_Request/cv/')

    def __str__(self):
          return "Joining Request from: " + self.First_Name + '  ' + self.Last_Name


class Submitted_Paper(models.Model):

    paper_id = models.CharField(max_length=10, default = random_string, unique = True)
    author = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phoneNo = PhoneNumberField()
    Country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    Article_Title = models.CharField(max_length=255, verbose_name="Article Title")
    Paper_Type = models.CharField(max_length=255, verbose_name="Paper Type")
    Subject_and_Category = models.CharField(max_length=255, verbose_name="Subject & Category")
    Abstract = models.TextField()
    paper = models.FileField(upload_to='Submitted_Article/papers/')

    def __str__(self):
          return self.author

class UserProfile(models.Model):
    
    Payment_Status= [
    ('Free', 'Free'),
    ('Premium', 'Premium'),
    ('Ultimate', 'Ultimate'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    FirstName = models.CharField(max_length= 150)
    LastName = models.CharField(max_length= 150)
    Email = models.CharField(max_length= 150, unique = True)
    PhoneNo = PhoneNumberField()
    Department = models.CharField(max_length= 150)
    Designation = models.CharField(max_length= 150)
    Institution = models.CharField(max_length= 150)
    Country = CountryField()
    Subscription = models.CharField(max_length= 15, verbose_name="Subscription Status", choices=Payment_Status, default='Free')

    # def __str__(self):
    #     return self.user.username
