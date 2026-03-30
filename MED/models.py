from django.db import models
from django.contrib.auth.models import User
import random

class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self): return self.name

# --- RE-ADDED PATIENT MODEL ---
class Patient(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True, null=True, blank=True)
    address = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.full_name

class Stock(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    class Meta:
        unique_together = ('branch', 'medicine')
    def __str__(self): return f"{self.medicine.name} at {self.branch.name}"

class Worker(models.Model):
    ROLE_CHOICES = [('Pharmacist', 'Pharmacist'), ('Rider', 'Rider'), ('Manager', 'Manager')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="Pharmacist")
    nin = models.CharField(max_length=20, unique=True, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    def __str__(self): return f"{self.user.username} ({self.role}) - {self.branch.name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'), ('Approved', 'Approved'), 
        ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Completed', 'Completed')
    ]
    patient_name = models.CharField(max_length=200)
    patient_phone = models.CharField(max_length=15, blank=True)
    medicines = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    delivery_code = models.CharField(max_length=4, editable=False)
    prescription_photo = models.ImageField(upload_to='prescriptions/', null=True, blank=True)
    latitude = models.FloatField(default=0.0, null=True, blank=True)
    longitude = models.FloatField(default=0.0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    processed_by = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.delivery_code:
            self.delivery_code = str(random.randint(1000, 9999))
        super().save(*args, **kwargs)