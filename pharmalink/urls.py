from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MED.urls')), # This connects to your app
    
    # These two lines fix the "Reverse for 'logout' not found" error
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='patient_portal'), name='logout'),
]