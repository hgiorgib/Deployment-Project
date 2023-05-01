observation = {'Gender': 'Male',
        'Married': 'No',
        'Dependents': "0",
        'Education': 'Graduate',
        'Self_Employed': 'No',
        'ApplicantIncome': 3000,
        'CoapplicantIncome': 0.0,
        'LoanAmount': 141,
        'Loan_Amount_Term': 360,
        'Credit_History': 1,
        'Property_Area': 'Urban'}

import requests
import json

url = 'http://ec2-18-217-43-51.us-east-2.compute.amazonaws.com:8000/predict'

response=requests.post(url, json=observation)
print(response.text)