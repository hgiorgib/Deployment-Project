from flask import Flask, jsonify, request
import pickle
import pandas as pd
import numpy as np

with open('loan_pred.pkl', 'rb') as f:
    pipeline = pickle.load(f)

 #Create an application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from post request
    data = request.get_json(force=True)
    print(data)
    data_df = pd.DataFrame(data, index=[0])
    # Predictions with trained model
    predictions = pipeline.predict(data_df)
  
    return jsonify(predictions.tolist())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000',debug=True)