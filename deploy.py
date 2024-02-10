import streamlit as st
import joblib
import pandas as pd
import xgboost

# Streamlit interface
st.title('Loan Default Prediction App')

# Streamlit app layout
st.write("Enter customer information:")

# Load the trained model
model = joblib.load('loan_default_prediction_xg.joblib')

# Function to make predictions
def predict_default(data):
    features = pd.DataFrame(data, index=[0])
    prediction = model.predict(features)
    return prediction[0]

# Function to map numeric prediction to labels
def map_prediction(prediction):
    return 'Default' if prediction == 1 else 'No Default'

# Input fields for the features with labels
age            = st.number_input('Age')
income         = st.number_input('Income')
loan_amount    = st.number_input('LoanAmount')
credit_score   = st.number_input('CreditScore')
months_employed= st.number_input('MonthsEmployed')
credit_lines   = st.number_input('NumCreditLines')
interest_rate  = st.number_input('InterestRate')
loan_term      = st.number_input('LoanTerm')
dti_ratio      = st.number_input('DTIRatio')
education      = st.radio("Education", ["Bachelor's", "Master's", 'High School', 'PhD'])
employment_type= st.radio('EmploymentType',['Full-time', 'Unemployed', 'Self-employed', 'Part-time'])
marital_status = st.radio('MaritalStatus',['Divorced', 'Married', 'Single'])
has_mortgage   = st.selectbox("HasMortgage", ['No', 'Yes'])
loan_purpose   = st.radio('LoanPurpose', ['Other', 'Auto', 'Business', 'Home', 'Education'])
has_cosigner   = st.selectbox("Has_Cosigner", ['No', 'Yes'])
has_dependents = st.selectbox("Has_Dependents", ['No', 'Yes'])


# Mapping for encoding
has_cosigner_mapping = {'No': 0, 'Yes': 1}
has_dependents_mapping = {'No': 0, 'Yes': 1}
has_mortgage_mapping = {'No': 0, 'Yes': 1}
education_mapping = {"Bachelor's": 0, "High School": 1, "Master's": 2, "PhD": 3}
loan_purpose_mapping = {'Auto': 0, 'Business': 1, 'Education': 2, 'Home': 3, 'Other': 4}
employment_type_mapping = {'Full-Time': 0, 'Part-time': 1, 'Self-employed': 2, 'Unemployed': 3}
marital_status_mapping = {'Divorced': 0, 'Married': 1, 'Single': 2}

# Convert labels to encoded values
education      = education_mapping[education]
employment_type= employment_type_mapping[employment_type]
marital_status = marital_status_mapping[marital_status]
has_mortgage   = has_mortgage_mapping[has_mortgage]
loan_purpose   = loan_purpose_mapping[loan_purpose]
has_cosigner   = has_cosigner_mapping[has_cosigner]
has_dependents = has_dependents_mapping[has_dependents]

# Make a prediction
features = {
    'Age': age, 'Income': income, 'LoanAmount': loan_amount,
    'CreditScore': credit_score, 'MonthsEmployed': months_employed,
    'NumCreditLines': credit_lines, 'InterestRate': interest_rate,
    'LoanTerm': loan_term, 'DTIRatio': dti_ratio, 'Education': education,
    'EmploymentType': employment_type, 'MaritalStatus': marital_status,
    'HasMortgage': has_mortgage, 'LoanPurpose': loan_purpose,
    'Has_Cosigner': has_cosigner, 'Has_Dependents': has_dependents
}

# Make a prediction

if st.button("Predict"):
    prediction = predict_default(features)
    mapped_prediction = map_prediction(prediction)
    st.success(f"The predicted status is: {mapped_prediction}")