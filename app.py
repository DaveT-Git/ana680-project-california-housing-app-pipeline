from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the saved pipeline (contains scaler + linear regression model)
pipeline = joblib.load('ca_housing_pipeline.pkl')

# Define the expected feature names (must match training)
FEATURES = ['MedInc', 'AveRooms', 'HouseAge', 'Latitude', 'Longitude']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', values={}, predict=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = {
            'MedInc': float(request.form['MedInc']),
            'AveRooms': float(request.form['AveRooms']),
            'HouseAge': float(request.form['HouseAge']),
            'Latitude': float(request.form['Latitude']),
            'Longitude': float(request.form['Longitude'])
        }

        input_df = pd.DataFrame([data])

        prediction_raw = pipeline.predict(input_df)[0]
        prediction_dollars = round(prediction_raw * 100000)

        # Format nice output message
        predict_text = f"Predicted Median House Value: ${prediction_dollars:,} " \
                       f"(${prediction_raw:.2f} × $100,000)"

        return render_template('index.html', values=data, predict=predict_text)

    except Exception as e:
        return render_template('index.html', values=request.form, predict=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)