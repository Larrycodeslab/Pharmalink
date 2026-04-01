from django.urls import path
from . import views

urlpatterns = [
    path('', views.pharmacy, name='pharmacy'),
    path('delete/<int:pharmacy_id>/', views.delete_pharmacy, name='delete_pharmacy'),
    path('update/<int:pharmacy_id>/', views.update_pharmacy, name='update_pharmacy'),
  
]