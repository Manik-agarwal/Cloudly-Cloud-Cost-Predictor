from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('Main_Model.pkl', 'rb'))
Instances = pd.read_csv('Instances.csv')
OS_types = pd.read_csv('OS_Types.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    instance_types = sorted(Instances['Instance Type'].unique())
    os_list = sorted(OS_types['OS'].unique())
    region = "east"  # Fixed region
    
    # Insert default options
    instance_types.insert(0, 'Select Instance Type')
    os_list.insert(0, 'Select OS')

    return render_template('index.html', instance_types=instance_types, os_list=os_list, region=region)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    instance_type = request.form.get('instance_type')  # Updated input field names
    os_type = request.form.get('os_type')
    region = "east"  # Region is fixed as 'east'
    
    # Create a DataFrame with user input
    input_data = pd.DataFrame([[instance_type, os_type, region]], columns=['Instance Type', 'OS', 'Region'])
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Return the result as a string with 2 decimal precision
    return str(np.round(prediction[0], 2))

if __name__ == '__main__':
    app.run()
