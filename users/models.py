# models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class PredictionResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    height = models.FloatField()
    weight = models.FloatField()
    temperature = models.FloatField()
    heart_rate = models.IntegerField()
    cholesterol = models.IntegerField()
    blood_sugar = models.IntegerField()
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    existing_conditions = models.CharField(max_length=255)
    family_history = models.CharField(max_length=255)
    smoking_status = models.CharField(max_length=255)
    predicted_disease = models.CharField(max_length=255)
    confidence_score = models.FloatField()

    # Automatically set the current timestamp when the record is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.predicted_disease} with {self.confidence_score}% confidence"

