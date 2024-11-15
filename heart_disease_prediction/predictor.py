import os
import pandas as pd
import numpy as np
import pickle
from typing import Dict, Any
from django.conf import settings

class HealthPredictor:
    def __init__(self):
        """Initialize the predictor by loading all necessary models and preprocessors"""
        self.knn_model = None
        self.scaler = None
        self.label_encoder = None
        self.onehot_encoder = None
        self.imputer = None
        self.load_models()

    def load_models(self) -> None:
        """Load all saved models and preprocessors from the models directory"""
        # Define the path to the models directory
        models_dir = os.path.join(settings.BASE_DIR, 'models')
        
        try:
            # Load each model file using the full path
            with open(os.path.join(models_dir, 'knn_model.pkl'), 'rb') as f:
                self.knn_model = pickle.load(f)
            
            with open(os.path.join(models_dir, 'scaler.pkl'), 'rb') as f:
                self.scaler = pickle.load(f)
            
            with open(os.path.join(models_dir, 'label_encoder.pkl'), 'rb') as f:
                self.label_encoder = pickle.load(f)
            
            with open(os.path.join(models_dir, 'onehot_encoder.pkl'), 'rb') as f:
                self.onehot_encoder = pickle.load(f)
            
            with open(os.path.join(models_dir, 'imputer_final.pkl'), 'rb') as f:
                self.imputer = pickle.load(f)
                
        except FileNotFoundError as e:
            raise Exception(
                "Model files not found. Please ensure all required model files "
                f"are present in the {models_dir} directory."
            ) from e
        except Exception as e:
            raise Exception(f"Error loading model files: {str(e)}") from e

    def validate_input(self, patient_data: Dict[str, Any]) -> None:
        """Validate the input data format and required fields"""
        required_fields = {
            'Height_cm', 'Weight_kg', 'Temperature_C', 'Heart_Rate',
            'Cholesterol_mg_dL', 'Blood_Sugar_mg_dL', 'Systolic', 'Diastolic',
            'Existing_Conditions', 'Family_History_Heart_Disease', 'Smoking_Status'
        }
        
        missing_fields = required_fields - set(patient_data.keys())
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
        
        # Additional validation for numerical fields
        numeric_fields = {
            'Height_cm': (0, 300),
            'Weight_kg': (0, 500),
            'Temperature_C': (0, 100),
            'Heart_Rate': (0, 200),
            'Cholesterol_mg_dL': (0, 500),
            'Blood_Sugar_mg_dL': (0, 500),
            'Systolic': (0, 250),
            'Diastolic': (0, 200)
        }
        
        for field, (min_val, max_val) in numeric_fields.items():
            value = patient_data[field]
            if not isinstance(value, (int, float)):
                raise ValueError(f"{field} must be a number")
            if value < min_val or value > max_val:
                raise ValueError(f"{field} must be between {min_val} and {max_val}")

    def prepare_input(self, patient_data: Dict[str, Any]) -> np.ndarray:
        """Prepare input data for prediction"""
        # Convert to DataFrame
        patient_df = pd.DataFrame([patient_data])
        
        # Separate categorical features
        categorical_features = ['Existing_Conditions', 'Family_History_Heart_Disease', 'Smoking_Status']
        
        try:
            # Encode categorical features
            categorical_encoded = self.onehot_encoder.transform(patient_df[categorical_features])
            
            # Combine numeric and encoded categorical features
            patient_numeric = patient_df.drop(columns=categorical_features)
            patient_preprocessed = np.hstack((patient_numeric.values, categorical_encoded))
            
            # Apply imputation
            patient_imputed = self.imputer.transform(patient_preprocessed)
            
            return patient_imputed
            
        except Exception as e:
            raise Exception(f"Error during data preparation: {str(e)}") from e

    def predict(self, patient_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make prediction for a single patient
        
        Args:
            patient_data (dict): Dictionary containing patient health information
            
        Returns:
            dict: Prediction result with disease and confidence score
        """
        try:
            # Validate input
            self.validate_input(patient_data)
            
            # Prepare input data
            patient_preprocessed = self.prepare_input(patient_data)
            
            # Scale the data
            patient_scaled = self.scaler.transform(patient_preprocessed)
            
            # Make prediction
            prediction_encoded = self.knn_model.predict(patient_scaled)
            prediction_proba = self.knn_model.predict_proba(patient_scaled)
            
            # Decode prediction
            predicted_disease = self.label_encoder.inverse_transform(prediction_encoded)[0]
            confidence_score = np.max(prediction_proba) * 100
            
            # Prepare detailed response
            response = {
                'predicted_disease': predicted_disease,
                'confidence_score': round(confidence_score, 2),
                # 'prediction_probabilities': {
                #     disease: round(prob * 100, 2)
                #     for disease, prob in zip(self.label_encoder.classes_, prediction_proba[0])
                # }
            }
            
            # Add prediction details
            response['details'] = {
                'model_type': 'K-Nearest Neighbors',
                'features_used': list(patient_data.keys())
            }
            
            return response
            
        except Exception as e:
            return {'error': str(e)}

