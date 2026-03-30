from django import forms
from .models import Patient, Order

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'phone_number', 'email', 'address']
        
        # This is where the Custom Interface happens!
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none transition-all',
                'placeholder': 'Enter full name...'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none transition-all',
                'placeholder': '+234...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none transition-all',
                'placeholder': 'name@example.com'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none transition-all',
                'rows': 3,
                'placeholder': 'Delivery address details...'
            }),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['patient_name', 'medicines', 'branch']
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none'}),
            'medicines': forms.Textarea(attrs={'class': 'w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none', 'rows': 3}),
            'branch': forms.Select(attrs={'class': 'w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl focus:ring-2 focus:ring-blue-500 outline-none'}),
        }