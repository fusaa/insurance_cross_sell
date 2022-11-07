import pickle

import pandas as pd
from flask import Flask, request, Response
import os
from healthinsurance import HealthInsurance

app = Flask(__name__)

# loads model
path = './'
model = pickle.load(open(path + 'model_log_regression.pkl', 'rb'))  # memory bank alt.

# API init
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()

    if test_json:
        if isinstance(test_json, dict):  # unique item
            test_raw = pd.DataFrame(test_json, index=[0])
        else:  # multiple items
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # start Rossmann class
        pipeline = HealthInsurance()

        # data cleaning
        df = pipeline.data_cleaning(test_raw)
        print(df.columns)
        # features
        df = pipeline.feature_engineering(df)

        # data prep
        df = pipeline.data_preparation(df)

        # prediction
        df = pipeline.get_prediction(model, test_raw, df)

        return df
    else:
        return Response('{}', status=200, mimetype='application/json')

@app.route('/pred', methods=['POST'])
def health_insurance_pred():
    test_json = request.get_json()

    if test_json:
        if isinstance(test_json, dict):  # unique item
            test_raw = pd.DataFrame(test_json, index=[0])
        else:  # multiple items
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # start Rossmann class
        pipeline = HealthInsurance()

        # data cleaning
        # df = pipeline.data_cleaning(test_raw)

        # features
        # df = pipeline.feature_engineering(df)

        # data prep
        # df = pipeline.data_preparation(df)

        # prediction
        df = pipeline.get_prediction(model, test_raw, test_raw)

        return df
    else:
        return Response('{}', status=200, mimetype='application/json')


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host = '0.0.0.0', port = port)
    # app.run('0.0.0.0', debug=True)