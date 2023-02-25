from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

CITY_CHOICES = (
    ('AB', 'Abeokuta'),
    ('IL', 'Ilorin'),
    ('ABJ', 'Abuja'),
    ('ADE', 'Ado-Ekiti')
    
)


class WaitList(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    
    def __str__(self):
        return self.email
    
    
    
class RiderRegister(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(unique=True)
    city = models.CharField(choices=CITY_CHOICES, max_length=3)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'