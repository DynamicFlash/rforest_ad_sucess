import pickle
from flask import Flask, request
import pandas as pd
import numpy as np

app = Flask(__name__)

with open('./Model/rfc.pkl', 'rb+') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods= ['POST'])
def greeting():
    msg = request.form["msg"]
    return "Hello " + msg

@app.route('/file_in', methods = ['POST'])
def social_media_ad_car():
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
def social_media_ad_car():
    age = request.args.get("age")
    est_sal = request.args.get("estimated_sal")

    prediction = model.predict(np.array([[age, est_sal]]))
    return str(prediction)

if __name__=='__main__':
    app.run()
