import pandas as pd
import pickle
import numpy as np
from PIL import Image
import streamlit as st

pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

def predict_output(dependents, education, self_employed, income, loan_amount, loan_term, cibil_score,
                    residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value):
    # Map string inputs to numerical values
    education_numeric = education_mapping_dict[education]
    self_employed_numeric = self_employed_mapping_dict[self_employed]

    prediction = model.predict([[dependents, education_numeric, self_employed_numeric, income, loan_amount, loan_term,
                                 cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value,
                                 bank_asset_value]])
    return prediction[0]

st.title("Loan Approval")

education_mapping_dict = {
    'Graduate': 0,
    'Not Graduate': 1,
}
self_employed_mapping_dict = {
    'No': 0,
    'Yes': 1,
}

loan_id = st.text_input("Loan Id ")
dependents = st.text_input("Dependents ")
education = st.selectbox("Education ", list(education_mapping_dict.keys()))
self_employed = st.selectbox("Self Employed ", list(self_employed_mapping_dict.keys()))
income = st.text_input("Income")
loan_amount = st.text_input("Loan Amount")
loan_term = st.text_input("Loan Term")
cibil_score = st.text_input("Cibil Score")
residential_assets_value = st.text_input("Residential Assets Value")
commercial_assets_value = st.text_input("Commercial Assets Value")
luxury_assets_value = st.text_input("Luxury Assets Value")
bank_asset_value = st.text_input("Bank Asset Value")
loan_status = ""

if st.button("Predict"):
    loan_status = predict_output(dependents, education, self_employed, income, loan_amount, loan_term, cibil_score,
                                 residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value)
    if loan_status == 0:
        st.success("Loan Approved!")
    else:
        st.error("Loan Rejected!")


# import pickle
# import streamlit as st
 
# pickle_in = open("rfc.pkl", "rb")
# rfc = pickle.load(pickle_in)
 
# def map_categorical_inputs(Education, EmploymentType, MaritalStatus, HasMortgage, HasDependents, LoanPurpose, HasCoSigner):
#     education_mapping = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
#     employment_mapping = {"Unemployed": 0, "Self-employed": 1, "Part-time": 2, "Full-time": 3}
#     marital_mapping = {"Single": 0, "Divorced": 1, "Married": 2}
#     mortgage_mapping = {"No": 0, "Yes": 1}
#     dependents_mapping = {"No": 0, "Yes": 1}
#     purpose_mapping = {"Other": 0, "Auto": 1, "Business": 2, "Education": 3, "Home": 4}
#     co_signer_mapping = {"No": 0, "Yes": 1}
 
#     mapped_education = education_mapping.get(Education, -1)
#     mapped_employment = employment_mapping.get(EmploymentType, -1)
#     mapped_marital = marital_mapping.get(MaritalStatus, -1)
#     mapped_mortgage = mortgage_mapping.get(HasMortgage, -1)
#     mapped_dependents = dependents_mapping.get(HasDependents, -1)
#     mapped_purpose = purpose_mapping.get(LoanPurpose, -1)
#     mapped_co_signer = co_signer_mapping.get(HasCoSigner, -1)
 
#     return mapped_education, mapped_employment, mapped_marital, mapped_mortgage, mapped_dependents, mapped_purpose, mapped_co_signer
 
# def predict_output(Age, Income, LoanAmount, CreditScore, MonthsEmployed, NumCreditLines, InterestRate, LoanTerm, DTIRatio,
#                    mapped_education, mapped_employment, mapped_marital, mapped_mortgage, mapped_dependents,
#                    mapped_purpose, mapped_co_signer):
#     prediction = rfc.predict([[Age, Income, LoanAmount, CreditScore, MonthsEmployed, NumCreditLines, InterestRate,
#                                LoanTerm, DTIRatio, mapped_education, mapped_employment, mapped_marital,
#                                mapped_mortgage, mapped_dependents, mapped_purpose, mapped_co_signer]])
#     return prediction[0]
 
# def main():
#     st.title("Welcome To Loan Default Prediction")
#     html_temp = """
# <div style ="background-color: tomato; padding: 10px">
# <h2 style ="color: white; text-align:center;">Streamlit Loan Default Prediction App </h2>
# </div>
#     """
#     st.markdown(html_temp, unsafe_allow_html=True)
#     Age = st.text_input("Age", "Type Here")
#     Income = st.text_input("Income", "Type Here")
#     LoanAmount = st.text_input("LoanAmount", "Type Here")
#     CreditScore = st.text_input("CreditScore", "Type Here")
#     MonthsEmployed = st.text_input("MonthsEmployed", "Type Here")
#     NumCreditLines = st.text_input("NumCreditLines", "Type Here")
#     InterestRate = st.text_input("InterestRate", "Type Here")
#     LoanTerm = st.text_input("LoanTerm", "Type Here")
#     DTIRatio = st.text_input("DTIRatio", "Type Here")
#     Education = st.radio("Education", ["High School", "Bachelor's", "Master's", "PhD"])
#     EmploymentType = st.radio("EmploymentType", ["Unemployed", "Self-employed", "Part-time", "Full-time"])
#     MaritalStatus = st.radio("LoanTerm", ["Single", "Divorced", "Married"])
#     HasMortgage = st.radio("HasMortgage", ["No", "Yes"])
#     HasDependents = st.radio("HasDependents", ["No", "Yes"])
#     LoanPurpose = st.radio("LoanPurpose", ["Other", "Auto", "Business", "Education", "Home"])
#     HasCoSigner = st.radio("HasCoSigner", ["No", "Yes"])
#     mapped_education, mapped_employment, mapped_marital, mapped_mortgage, mapped_dependents, mapped_purpose, mapped_co_signer = map_categorical_inputs(
#         Education, EmploymentType, MaritalStatus, HasMortgage, HasDependents, LoanPurpose, HasCoSigner)
#     result = ""
#     if st.button("Predict"):
#         result = predict_output(Age, Income, LoanAmount, CreditScore, MonthsEmployed, NumCreditLines, InterestRate,
#                                 LoanTerm, DTIRatio, mapped_education, mapped_employment, mapped_marital,
#                                 mapped_mortgage, mapped_dependents, mapped_purpose, mapped_co_signer)
#     st.success(f'The Output is {result}')
 
# if __name__ == "__main__":
#     main()