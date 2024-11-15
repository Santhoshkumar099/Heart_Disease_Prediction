# users/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('successfully_registered/', views.successfully_registered, name='successfully_registered'),
    path('successfully_logged_in/', views.successfully_logged_in, name='successfully_logged_in'),
    # Prediction-related URL (main prediction form page)
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('view_history/', views.view_history, name='view_history'),
    path('predict/', views.prediction_view, name='prediction_view'),
    path('logout/', views.logout_view, name='logout'),
    
]
