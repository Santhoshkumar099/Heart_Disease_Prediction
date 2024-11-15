from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class HealthPredictionForm(forms.Form):
    height = forms.FloatField(
        label='Height (cm)', 
        min_value=0, 
        max_value=300,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    weight = forms.FloatField(
        label='Weight (kg)', 
        min_value=0, 
        max_value=500,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    temperature = forms.FloatField(
        label='Temperature (°C)', 
        min_value=0, 
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    heart_rate = forms.FloatField(
        label='Heart Rate', 
        min_value=0, 
        max_value=200,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    cholesterol = forms.FloatField(
        label='Cholesterol (mg/dL)', 
        min_value=0, 
        max_value=500,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    blood_sugar = forms.FloatField(
        label='Blood Sugar (mg/dL)', 
        min_value=0, 
        max_value=500,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    systolic = forms.FloatField(
        label='Systolic Pressure', 
        min_value=0, 
        max_value=250,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    diastolic = forms.FloatField(
        label='Diastolic Pressure', 
        min_value=0, 
        max_value=200,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    existing_conditions = forms.ChoiceField(
        choices=[
            ('Diabetes', 'Diabetes'),
            ('Hypertension', 'Hypertension'),
            ('High Cholesterol', 'High Cholesterol'),
            ('Asthma', 'Asthma'),
            ('Unknown', 'Unknown')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    family_history = forms.ChoiceField(
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No'),
            ('Unknown', 'Unknown')
        ],
        label='Family History of Heart Disease',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    smoking_status = forms.ChoiceField(
        choices=[
            ('Never', 'Never'),
            ('Former', 'Former'),
            ('Current', 'Current'),
            ('Unknown', 'Unknown')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )