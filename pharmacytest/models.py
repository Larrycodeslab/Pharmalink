from django.db import models

# Create your models here.
class Pharmacy(models.Model):
        name = models.CharField(max_length=100)
        address = models.CharField(max_length=200)
        owner_name = models.CharField(max_length=100)
        pharmacy_license_number = models.CharField(max_length=50)
        phone_number = models.CharField(max_length=20)
    
        def __str__(self):
            return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.name