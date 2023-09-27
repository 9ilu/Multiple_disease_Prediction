import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('C:/Users/HP/Desktop/multiple_disease_predictive_system/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(
    open('C:/Users/HP/Desktop/multiple_disease_predictive_system/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(
    open('C:/Users/HP/Desktop/multiple_disease_predictive_system/parkinsons_model.sav', 'rb'))

# sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System Using ML',
                                    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction']
                                   ,icons = ['activity','heart','person'] ,default_index = 0)

# Diabetes Predictive Page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the users
    # columns for the input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_dignosis = ''

    # creating a button for prediction

    if st.button('Diabetes Test Result'):
        diab_Prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_Prediction[0] == 1:
            diab_dignosis = 'The person is Diabetic'
        else:
            diab_dignosis = 'The person is Not Diabetic'

    st.success(diab_dignosis)

if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestorol is mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by  flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''

    # creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

if selected == 'Parkinsons Prediction':
    # page title
    st.title('Parkinsons Disease Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        lit_p = st.text_input('MDVP:_litre(%)')

    with col5:
        lit_a = st.text_input('MDVP:_litre(abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PRQ = st.text_input('MDVP:PRQ')

    with col3:
        DDP = st.text_input('MDVP:DDP')

    with col4:
        shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        shimmer_db = st.text_input('MDVP:Shimmer(db)')

    with col1:
        shimmer_apq3 = st.text_input('Shimmer:APQ3')

    with col2:
        shimmer_apq5 = st.text_input('Shimmer:APQ5')

    with col3:
        shimmer_apq = st.text_input('MDVP:APQ')

    with col4:
        shimmer_dda = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PRE = st.text_input('PRE')

    Parkinsons_diagnosis = ''

    if st.button('Parkinsons Disease Test Result'):
        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, lit_p, lit_a, RAP, PRQ, DDP, shimmer, shimmer_db, shimmer_apq3, shimmer_apq5, shimmer_apq,
              shimmer_dda, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PRE]])
        if parkinsons_prediction[0] == 1:
            Parkinsons_diagnosis = 'The person is having Parkinsons disease'
        else:
            Parkinsons_diagnosis = 'The person does not have any Parkinsons disease'

    st.success(Parkinsons_diagnosis)
