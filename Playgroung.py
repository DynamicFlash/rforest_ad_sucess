import pickle
from flask import Flask, request
import pandas as pd
import numpy as np

app = Flask(__name__)

with open('./Model/prfc.pkl', 'rb+') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods= ['POST'])
def greeting():
    msg = request.form["msg"]
    return "Hello " + msg

@app.route('/file_in', methods = ['POST'])
def social_media_ad_car_file():
    """Example file endpoint returning a prediction of ad
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))

@app.route('/single_in', methods = ['POST'])
def social_media_ad_car_sig():
    age = request.form["age"]
    est_sal = request.form["estimated_sal"]
    prediction = model.predict(np.array([[age, est_sal]]))
    return str(prediction)

if __name__=='__main__':
    app.run(port=8000)
