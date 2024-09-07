from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd 
import numpy as np


app = Flask(__name__)

# Dummy function to simulate price prediction
def predict_price(instance_type, operating_system, region):
    # Implement your actual prediction logic here
    # For now, it returns a dummy price based on the input
    return 100.0  # Dummy price

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    instance_type = request.form['instance_type']
    operating_system = request.form['operating_system']
    region = request.form['region']
    
    price = predict_price(instance_type, operating_system, region)
    
    return render_template('result.html', instance_type=instance_type, 
                           operating_system=operating_system, region=region, price=price)

if __name__ == '__main__':
    app.run(debug=True)
