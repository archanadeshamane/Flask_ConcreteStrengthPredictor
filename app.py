#Student Name: Archana Deshamane
#MIS NO: 752462002
#Batch: 01
#Problem statement: To predict Concrete strength, save model using pickle and Display result using Flask.

from flask import Flask,render_template,request , redirect, url_for
import numpy as np
import pickle

app= Flask(__name__)

concrete = open("concrete.pkl", "rb")
concrete_model = pickle.load(concrete)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            Cement = float(request.form['Cement'])
            Blast = float(request.form['Blast'])
            Fly = float(request.form['Fly'])
            Water = float(request.form['Water'])
            Superplasticizer = float(request.form['Superplasticizer'])
            Coarse = float(request.form['Coarse'])
            Fine = float(request.form['Fine'])
            Age = float(request.form['Age'])
            pred_args = [[Cement, Blast, Fly, Water, Superplasticizer, Coarse, Fine,Age]]
            pred_args_arr = np.array(pred_args)
            model_prediction = concrete_model.predict(pred_args_arr)
            model_prediction = round(float(model_prediction), 2)  
        except ValueError:
            return "Please check if the values are entered correctly.  Kindly Re-enter correct values and then, try again."
                 
    return render_template('predict.html', prediction = model_prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
