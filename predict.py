### Loading the model
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask
from flask import request
from flask import jsonify



model_file = 'model_C=1.0.bin'



with open(model_file, 'rb') as f_in:
   scaler, model = pickle.load(f_in)

app = Flask('churn')

scaler, model



#patient = np.array(X_test.iloc[0])
#patient = patient.reshape(1, -1)
#[1].to_dict()
@app.route('/predict', methods=['POST'])
def predict():

    patient = request.get_json()

    p1 = pd.DataFrame.from_records(patient, index=[0])
    xyz = scaler.fit_transform(p1)
    y_pred = model.predict_proba(xyz)[0,1]
    pred = y_pred >= 0.5

    result = {
        'Insurance_probabililty': float(y_pred),
        'Insurance': bool(pred)
    }

    return jsonify(result)
#abc[0]

#print('Model prediction is:',abc)



def ping():
    return "PONG"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)