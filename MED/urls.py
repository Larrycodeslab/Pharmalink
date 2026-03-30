from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_portal, name='patient_portal'),
    path('orders/', views.order_list, name='order_list'),
    path('approve/<int:order_id>/', views.approve_order, name='approve_order'),
    path('rider/', views.rider_dashboard, name='rider_dashboard'),
    path('track/<int:order_id>/', views.track_order, name='track_order'),
    path('update-location/<int:order_id>/', views.update_location, name='update_location'),
    path('branch/<int:branch_id>/inventory/', views.branch_inventory, name='branch_inventory'),
    path('branch/<int:branch_id>/dashboard/', views.branch_dashboard, name='branch_dashboard'),
]