from django.shortcuts import render, redirect
from .forms import RegisterForm, HealthPredictionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import PredictionResult
import os
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.conf import settings
from .forms import HealthPredictionForm
from .models import PredictionResult
from heart_disease_prediction.predictor import HealthPredictor

def home(request):
    return render(request, 'home.html')

def successfully_registered(request):
    return render(request, 'users/successfully_registered.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('successfully_registered')
    
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required  # Ensure the user is logged in before accessing this view
def successfully_logged_in(request):
    return render(request, 'users/successfully_logged_in.html')

# def login_view(request):  #dont name "login" bcoz django already have build-in log in function"
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('prediction_view')  # Redirect prediction view
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})


@login_required
def prediction_view(request):
    if request.method == 'POST':
        form = HealthPredictionForm(request.POST)
        if form.is_valid():
            # Get cleaned data from form
            patient_data = {
                'Height_cm': form.cleaned_data['height'],
                'Weight_kg': form.cleaned_data['weight'],
                'Temperature_C': form.cleaned_data['temperature'],
                'Heart_Rate': form.cleaned_data['heart_rate'],
                'Cholesterol_mg_dL': form.cleaned_data['cholesterol'],
                'Blood_Sugar_mg_dL': form.cleaned_data['blood_sugar'],
                'Systolic': form.cleaned_data['systolic'],
                'Diastolic': form.cleaned_data['diastolic'],
                'Existing_Conditions': form.cleaned_data['existing_conditions'],
                'Family_History_Heart_Disease': form.cleaned_data['family_history'],
                'Smoking_Status': form.cleaned_data['smoking_status']
            }

            # Initialize predictor and make prediction
            predictor = HealthPredictor()
            result = predictor.predict(patient_data)

            if result and 'error' not in result:
                # Check if the result has the expected keys
                if 'predicted_disease' in result and 'confidence_score' in result:
                    # Save prediction to database
                    prediction = PredictionResult(
                        user=request.user,
                        height=patient_data['Height_cm'],
                        weight=patient_data['Weight_kg'],
                        temperature=patient_data['Temperature_C'],
                        heart_rate=patient_data['Heart_Rate'],
                        cholesterol=patient_data['Cholesterol_mg_dL'],
                        blood_sugar=patient_data['Blood_Sugar_mg_dL'],
                        systolic=patient_data['Systolic'],
                        diastolic=patient_data['Diastolic'],
                        existing_conditions=patient_data['Existing_Conditions'],
                        family_history=patient_data['Family_History_Heart_Disease'],
                        smoking_status=patient_data['Smoking_Status'],
                        predicted_disease=result['predicted_disease'],
                        confidence_score=result['confidence_score']
                    )
                    prediction.save()

                    return render(request, 'users/result.html', {
                        'result': result,
                        'patient_data': patient_data
                    })
                else:
                    # Handle case where result doesn't have expected keys
                    return render(request, 'predictor/error.html', {
                        'error_message': 'Prediction result is incomplete or invalid.'
                    })
            else:
                # Handle prediction failure or error
                return render(request, 'predictor/error.html', {
                    'error_message': 'Prediction failed. Please try again later.'
                })
    else:
        form = HealthPredictionForm()

    return render(request, 'users/predictionform.html', {'form': form})

def login_view(request):  #dont name "login" bcoz django already have build-in log in function"
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_view')  # Redirect prediction view
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PredictionResult

@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')


@login_required
def view_history(request):
    # Get the user's prediction history (assuming predictions are stored with a user reference)
    history = PredictionResult.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'users/view_history.html', {'history': history})



def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('login')  # Redirects the user to the login page
