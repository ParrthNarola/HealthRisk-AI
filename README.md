# 🩺 HealthRisk AI - Multiple Disease Prediction System

A comprehensive machine learning-based web application that predicts the risk of multiple diseases using medical data. This project provides an interactive interface for healthcare professionals and individuals to assess their risk for Diabetes, Heart Disease, and Parkinson's Disease.

## 🚀 Features

### 🧃 Diabetes Prediction

- Predicts diabetes risk based on medical parameters
- Input parameters include:
  - Pregnancies count
  - Glucose level
  - Blood pressure
  - Skin thickness
  - Insulin level
  - BMI (Body Mass Index)
  - Diabetes pedigree function
  - Age

### ❤️ Heart Disease Prediction

- Assesses heart disease risk using comprehensive cardiac data
- Input parameters include:
  - Age and sex
  - Chest pain type
  - Resting blood pressure
  - Cholesterol levels
  - Fasting blood sugar
  - Resting ECG results
  - Maximum heart rate
  - Exercise-induced angina
  - ST depression
  - Number of major vessels
  - Thalassemia type

### 🧠 Parkinson's Disease Detection

- Detects Parkinson's disease using voice measurement features
- Analyzes 22 different voice-related parameters including:
  - Fundamental frequency (Fo, Fhi, Flo)
  - Jitter and shimmer measurements
  - Harmonic-to-noise ratio (HNR)
  - Nonlinear dynamic complexity measures
  - Signal fractal scaling exponent

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Machine Learning**: Scikit-learn, NumPy
- **Data Processing**: Pandas
- **Model Persistence**: Pickle
- **Development**: Jupyter Notebooks

## 📁 Project Structure

```
HealthRisk AI/
├── HealthRisk AI.py              # Main Streamlit application
├── saved models/                 # Trained ML models
│   ├── Diabetes_trained_model.sav
│   ├── Heart_trained_model.sav
│   └── parkinson_trained_model.sav
├── Diabetes predection/          # Diabetes prediction module
│   ├── diabetes.csv             # Diabetes dataset
│   └── project_diabetes_prediction.ipynb
├── Heart Disease/               # Heart disease prediction module
│   ├── heart_disease_data.csv   # Heart disease dataset
│   └── Heart_disease_prediction.ipynb
└── Parkinson_s Disease/         # Parkinson's disease detection module
    ├── parkinsons.csv          # Parkinson's dataset
    └── Parkinson_s_Disease_Detection.ipynb
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd "HealthRisk AI"
   ```

2. **Install required dependencies**

   ```bash
   pip install streamlit numpy pandas scikit-learn
   ```

3. **Run the application**

   ```bash
   streamlit run "HealthRisk AI.py"
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:8501`

## 📖 Usage Guide

### Getting Started

1. Launch the application using the command above
2. Use the sidebar to select the disease prediction model you want to use
3. Fill in the required medical parameters
4. Click the "Predict" button to get your risk assessment

### Input Guidelines

#### For Diabetes Prediction:

- **Pregnancies**: Number of times pregnant (0-20)
- **Glucose**: Plasma glucose concentration (0-200 mg/dL)
- **Blood Pressure**: Diastolic blood pressure (0-150 mm Hg)
- **Skin Thickness**: Triceps skin fold thickness (0-100 mm)
- **Insulin**: 2-Hour serum insulin (0-900 μU/ml)
- **BMI**: Body mass index (0-70 kg/m²)
- **Diabetes Pedigree Function**: Diabetes family history (0-2.5)
- **Age**: Age in years (1-120)

#### For Heart Disease Prediction:

- **Age**: Age in years (1-120)
- **Sex**: Gender (0 = Female, 1 = Male)
- **Chest Pain Type**: Type of chest pain (0-3)
- **Resting BP**: Resting blood pressure (80-200 mm Hg)
- **Cholesterol**: Serum cholesterol (100-600 mg/dL)
- **Fasting Blood Sugar**: > 120 mg/dL (0 = No, 1 = Yes)
- **Resting ECG**: Resting electrocardiographic results (0-2)
- **Max Heart Rate**: Maximum heart rate achieved (60-210 bpm)
- **Exercise Angina**: Exercise-induced angina (0 = No, 1 = Yes)
- **Oldpeak**: ST depression induced by exercise (0-6 mm)
- **ST Slope**: Slope of peak exercise ST segment (0-2)
- **Major Vessels**: Number of major vessels (0-3)
- **Thal**: Thalassemia type (0 = Normal, 1 = Fixed, 2 = Reversible)

#### For Parkinson's Disease Detection:

- Input 22 voice measurement features including fundamental frequency, jitter, shimmer, and other acoustic parameters

## 🔬 Model Information

### Training Data

- **Diabetes**: 769 samples with 8 features
- **Heart Disease**: 305 samples with 13 features
- **Parkinson's**: 197 samples with 22 features

### Model Performance

The models have been trained and optimized for accuracy using machine learning algorithms. Each model provides binary classification (disease present/absent) based on the input parameters.

## ⚠️ Important Notes

### Medical Disclaimer

- This application is for educational and research purposes only
- It should not be used as a substitute for professional medical advice
- Always consult with healthcare professionals for proper diagnosis
- The predictions are based on statistical models and may not be 100% accurate

### Data Privacy

- All data entered is processed locally and not stored
- No personal information is transmitted or saved
- The application runs entirely on your local machine

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Parth Narola**

- GitHub: [@parthnarola](https://github.com/parthnarola)

## 🙏 Acknowledgments

- Dataset providers for making the medical data publicly available
- Streamlit team for the excellent web framework
- Scikit-learn community for the machine learning tools
- Medical professionals who provided domain expertise

---

**Note**: This project is designed for educational purposes and should not replace professional medical consultation. Always seek advice from qualified healthcare providers for medical decisions.
