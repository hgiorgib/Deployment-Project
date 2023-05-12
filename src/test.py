observation = {'LoanAmount': 141,
        'Loan_Amount_Term': 360,
        'Log_LoanAmount': 1.819544,
        'total_income': 4900,
        'Log_total_income': 3.784689,
        'Married_No': 1,
        'Married_Yes': 0,
        'Dependents_0': 1,
        'Dependents_1': 0,
        'Dependents_2': 0,
        'Dependents_3+': 0,
        'Education_Graduate': 1,
        'Education_Not Graduate': 0,
        'Credit_History_0.0': 0,
        'Credit_History_1.0': 1,
        'Property_Area_Rural': 0,
        'Property_Area_Semiurban': 0,
        'Property_Area_Urban': 1,
}

import requests
import json

url = 'http://ubuntu@ec2-18-217-43-51.us-east-2.compute.amazonaws.com:5000/predict'

response=requests.post(url, json=observation)
print(response.json())