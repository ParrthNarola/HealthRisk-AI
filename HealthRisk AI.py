import streamlit as st
import numpy as np
import pickle

# Set page configuration
st.set_page_config(
    page_title="HealthRisk AI",
    page_icon="🧬",
    layout="wide"
)

# Load models
diabetes_model = pickle.load(open("/Users/parthnarola/Desktop/HealthRisk AI /saved models/Diabetes_trained_model.sav", 'rb'))
heart_model = pickle.load(open("/Users/parthnarola/Desktop/HealthRisk AI /saved models/Heart_trained_model.sav", 'rb'))
parkinson_model = pickle.load(open('/Users/parthnarola/Desktop/HealthRisk AI /saved models/parkinson_trained_model.sav', 'rb'))

# Sidebar navigation
st.sidebar.title("🧪 Multi-Disease Predictor")
st.sidebar.markdown("Choose which disease prediction model you want to use:")
selected_model = st.sidebar.selectbox(
    "Select Prediction Model", 
    ("Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction")
)

st.title("🩺 HealthRisk AI : Multiple Disease Predictor System")
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True
)

# =========================== Diabetes UI ==============================
if selected_model == "Diabetes Prediction":
    st.subheader("🧃 Diabetes Risk Check")

    with st.expander("ℹ️ About"):
        st.write("This model predicts the likelihood of diabetes based on medical inputs.")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Pregnancies", 0, 20)
        BloodPressure = st.number_input("Blood Pressure", 0, 150)
        Insulin = st.number_input("Insulin Level", 0.0, 900.0)

    with col2:
        Glucose = st.number_input("Glucose Level", 0, 200)
        SkinThickness = st.number_input("Skin Thickness", 0, 100)
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", 0.0, 2.5)

    with col3:
        BMI = st.number_input("BMI", 0.0, 70.0)
        Age = st.number_input("Age", 1, 120)

    if st.button("🔍 Predict Diabetes"):
        input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                Insulin, BMI, DiabetesPedigreeFunction, Age]])
        prediction = diabetes_model.predict(input_data)

        if prediction[0] == 1:
            st.error("🚨 The person is likely to have **Diabetes**.")
        else:
            st.success("✅ The person is not likely to have **Diabetes**.")

# =========================== Heart UI ==============================
elif selected_model == "Heart Disease Prediction":
    st.subheader("❤️ Heart Disease Risk Checker")

    with st.expander("ℹ️ About"):
        st.write("This model predicts the presence of heart disease using patient data.")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", 1, 120)
        sex = st.selectbox("Sex", [0, 1])
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])

    with col2:
        trestbps = st.number_input("Resting BP", 80, 200)
        chol = st.number_input("Cholesterol", 100, 600)
        restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
        exang = st.selectbox("Exercise Induced Angina", [0, 1])

    with col3:
        thalach = st.number_input("Max Heart Rate", 60, 210)
        oldpeak = st.number_input("Oldpeak", 0.0, 6.0)
        slope = st.selectbox("ST Slope", [0, 1, 2])
        ca = st.selectbox("No. of major vessels", [0, 1, 2, 3])
        thal = st.selectbox("Thal (0=normal, 1=fixed, 2=reversible)", [0, 1, 2])

    if st.button("🔍 Predict Heart Disease"):
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                thalach, exang, oldpeak, slope, ca, thal]])
        prediction = heart_model.predict(input_data)

        if prediction[0] == 1:
            st.error("🚨 The person is likely to have **Heart Disease**.")
        else:
            st.success("✅ The person is not likely to have **Heart Disease**.")

# =========================== Parkinson's UI ==============================
elif selected_model == "Parkinson's Prediction":
    st.subheader("🧠 Parkinson’s Disease Screening")

    with st.expander("ℹ️ About"):
        st.write("This model detects signs of Parkinson’s using voice measurements.")

    st.markdown("🗣️ Please input the following voice-related features:")

    features = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
        "RPDE", "DFA", "Spread1", "Spread2", "D2", "PPE"
    ]

    input_vals = []
    cols = st.columns(3)
    for i, feat in enumerate(features):
        val = cols[i % 3].number_input(feat)
        input_vals.append(val)

    if st.button("🔍 Predict Parkinson's"):
        input_data = np.array([input_vals])
        prediction = parkinson_model.predict(input_data)

        if prediction[0] == 1:
            st.error("🚨 The person is likely to have **Parkinson’s Disease**.")
        else:
            st.success("✅ The person is not likely to have **Parkinson’s Disease**.")


# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # loading saved model

# diabetes_model = pickle.load(open('/Users/parthnarola/Desktop/HealthRisk AI /saved moels/Diabetes_trained_model.sav','rb'))

# heart_disease_model = pickle.load(open('/Users/parthnarola/Desktop/HealthRisk AI /saved moels/Heart_trained_model.sav','rb'))

# parkinsons_model = pickle.load(open('/Users/parthnarola/Desktop/HealthRisk AI /saved moels/parkinson_trained_model.sav','rb'))

# #sidebar for navigator

# with st.sidebar:
    
#     selected = option_menu("Multiple Disease Prediction System",
#                            ['Diabetes Prediction',
#                             'Heart Disease prediction',
#                             'Parkinsons Prediction'],
#                            default_index = 0 )
    
# # Diabetes prediction page 
# if(selected == "Diabetes Prediction"):
    
#     # page title
#     st.title("Diabetes Prediction Using ML")
        
# if(selected == 'Heart Disease Predection'):
    
#     # Page title
#     st.title("Heart Disease Prediction using ML")
    
# if(selected == 'Parkinsons Disease Predection'):
    
#     # Page title
#     st.title("Parkinsons Prediction using ML")
    
    
    
    
    
    
    
    
    
    
    
    
    
# import streamlit as st
# import pickle
# import numpy as np

# # Load all three models
# diabetes_model = pickle.load(open("/Users/parthnarola/Desktop/HealthRisk AI /saved models/Diabetes_trained_model.sav", 'rb'))
# heart_model = pickle.load(open("/Users/parthnarola/Desktop/HealthRisk AI /saved models/Heart_trained_model.sav", 'rb'))
# parkinson_model = pickle.load(open('/Users/parthnarola/Desktop/HealthRisk AI /saved models/parkinson_trained_model.sav', 'rb'))

# # Sidebar selection
# st.sidebar.title("Disease Prediction App")
# selected_model = st.sidebar.selectbox(
#     "Select Prediction Model", 
#     ("Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction")
# )

# st.title("Multi-Disease Prediction System")

# # Diabetes Model UI
# if selected_model == "Diabetes Prediction":
#     st.header("Diabetes Prediction")

#     Pregnancies = st.number_input("Pregnancies", 0, 20, step=1)
#     Glucose = st.number_input("Glucose Level", 0, 200)
#     BloodPressure = st.number_input("Blood Pressure", 0, 150)
#     SkinThickness = st.number_input("Skin Thickness", 0, 100)
#     Insulin = st.number_input("Insulin Level", 0.0, 900.0)
#     BMI = st.number_input("BMI", 0.0, 70.0)
#     DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", 0.0, 2.5)
#     Age = st.number_input("Age", 1, 120, step=1)

#     if st.button("Predict Diabetes"):
#         input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
#                                 Insulin, BMI, DiabetesPedigreeFunction, Age]])
#         prediction = diabetes_model.predict(input_data)

#         if prediction[0] == 1:
#             st.error("The person is likely to have Diabetes.")
#         else:
#             st.success("The person is not likely to have Diabetes.")

# # Heart Disease Model UI
# elif selected_model == "Heart Disease Prediction":
#     st.header("Heart Disease Prediction")

#     age = st.number_input("Age", 1, 120)
#     sex = st.selectbox("Sex", [0, 1])  # 1 = male; 0 = female
#     cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
#     trestbps = st.number_input("Resting Blood Pressure", 80, 200)
#     chol = st.number_input("Cholesterol", 100, 600)
#     fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
#     restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
#     thalach = st.number_input("Max Heart Rate", 60, 210)
#     exang = st.selectbox("Exercise Induced Angina", [0, 1])
#     oldpeak = st.number_input("Oldpeak", 0.0, 6.0)
#     slope = st.selectbox("Slope of peak exercise ST segment", [0, 1, 2])
#     ca = st.selectbox("Number of major vessels (0-3)", [0, 1, 2, 3])
#     thal = st.selectbox("Thal (0=normal; 1=fixed defect; 2=reversible defect)", [0, 1, 2])

#     if st.button("Predict Heart Disease"):
#         input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
#                                 thalach, exang, oldpeak, slope, ca, thal]])
#         prediction = heart_model.predict(input_data)

#         if prediction[0] == 1:
#             st.error("The person is likely to have Heart Disease.")
#         else:
#             st.success("The person is not likely to have Heart Disease.")

# # Parkinson's Model UI
# elif selected_model == "Parkinson's Prediction":
#     st.header("Parkinson’s Disease Prediction")

#     fo = st.number_input("MDVP:Fo(Hz)")
#     fhi = st.number_input("MDVP:Fhi(Hz)")
#     flo = st.number_input("MDVP:Flo(Hz)")
#     jitter_percent = st.number_input("MDVP:Jitter(%)")
#     jitter_abs = st.number_input("MDVP:Jitter(Abs)")
#     rap = st.number_input("MDVP:RAP")
#     ppq = st.number_input("MDVP:PPQ")
#     ddp = st.number_input("Jitter:DDP")
#     shimmer = st.number_input("MDVP:Shimmer")
#     shimmer_db = st.number_input("MDVP:Shimmer(dB)")
#     apq3 = st.number_input("Shimmer:APQ3")
#     apq5 = st.number_input("Shimmer:APQ5")
#     apq = st.number_input("MDVP:APQ")
#     dda = st.number_input("Shimmer:DDA")
#     nhr = st.number_input("NHR")
#     hnr = st.number_input("HNR")
#     rpde = st.number_input("RPDE")
#     dfa = st.number_input("DFA")
#     spread1 = st.number_input("Spread1")
#     spread2 = st.number_input("Spread2")
#     d2 = st.number_input("D2")
#     ppe = st.number_input("PPE")

#     if st.button("Predict Parkinson's"):
#         input_data = np.array([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq,
#                                 ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr,
#                                 hnr, rpde, dfa, spread1, spread2, d2, ppe]])
#         prediction = parkinson_model.predict(input_data)

#         if prediction[0] == 1:
#             st.error("The person is likely to have Parkinson’s Disease.")
#         else:
#             st.success("The person is not likely to have Parkinson’s Disease.")
