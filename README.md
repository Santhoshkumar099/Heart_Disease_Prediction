# Heart Disease Prediction Web Application

A machine learning-powered web application that predicts the likelihood of heart disease based on various health parameters. The application is built using Django framework and uses a KNN (K-Nearest Neighbors) model for predictions.

## 🔗 Live Demo
[Heart Disease Prediction App](https://heart-disease-prediction-0hz4.onrender.com)

## 🌟 Features

- User Registration and Authentication
- Secure Login System
- Health Parameters Input Form
- Real-time Heart Disease Prediction
- Prediction History Tracking
- User Dashboard
- Mobile-Responsive Design

## 💻 Technical Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Machine Learning**: 
  - Algorithm: K-Nearest Neighbors (KNN)
  - Libraries: scikit-learn, pandas, numpy
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Deployment**: Render

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository
```bash
git clone [[your-repository-link]](https://github.com/Santhoshkumar099/Heart_disease_Prediction/tree/master)
cd heart-disease-prediction
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up the database
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

## 🔍 Usage

1. Register a new account or login with existing credentials
2. Navigate to the prediction form
3. Enter the required health parameters:
   - Height (cm)
   - Weight (kg)
   - Temperature (°C)
   - Heart Rate
   - Cholesterol (mg/dL)
   - Blood Sugar (mg/dL)
   - Blood Pressure (Systolic/Diastolic)
   - Existing Conditions
   - Family History
   - Smoking Status
4. Submit the form to get prediction results
5. View prediction history in the dashboard

## 🎯 Model Information

The heart disease prediction model uses the K-Nearest Neighbors algorithm, which was chosen for its:
- Effectiveness in classification tasks
- Ability to handle non-linear relationships
- Simple implementation and interpretation
- Good performance with medical data

### Data Preprocessing Steps:
- Feature scaling
- Handling missing values
- Feature engineering
- Data normalization

## 🔒 Security Features

- User authentication required for predictions
- Password hashing
- Form validation
- CSRF protection
- Secure session management

## 📱 Responsive Design

The application is fully responsive and works seamlessly across:
- Desktop computers
- Tablets
- Mobile devices

## 🛠️ Future Improvements

- Integration of additional machine learning models
- Enhanced data visualization
- Export functionality for prediction history
- API endpoints for external integration
- Advanced user profile management

## 📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details

## 👨‍💻 Author

Santhosh Kumar



## 📞 Support

For support, please contact [sksanthoshhkumar99@gmail.com]
