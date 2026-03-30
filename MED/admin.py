from django.contrib import admin
from .models import Worker, Patient, Branch, Order, Medicine, Stock

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    # 'user', 'role', and 'branch' are the new fields in our Worker model
    list_display = ('user', 'role', 'branch', 'is_active')
    list_filter = ('branch', 'role')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')
    search_fields = ('full_name', 'phone_number')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Added 'total_price' to the display so you can see sales at a glance
    list_display = ('patient_name', 'branch', 'status', 'total_price', 'delivery_code')
    list_filter = ('branch', 'status', 'created_at')
    readonly_fields = ('delivery_code', 'created_at')

# Added these so you can add Medicines and set their Prices per Branch
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'branch', 'price', 'quantity')
    list_filter = ('branch', 'medicine')