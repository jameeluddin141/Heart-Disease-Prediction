from flask import Flask,render_template,url_for,request
import pickle
from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
clf = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('heart.html')

@app.route('/predict', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return (render_template('heart.html'))


    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp =  request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']

        fbs = request.form['fbs']
        restecg = request.form['restecg']
        oldpeak = request.form['oldpeak']
        thalach = request.form['thalach']
        exang = request.form['exang']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        input_variables = pd.DataFrame([[age, sex, cp, trestbps,chol, fbs, restecg, oldpeak, thalach, exang, slope,ca,thal]],
                                       columns=['age', 'sex', 'cp', 'trestbps','chol', 'fbs',
                                                'restecg', 'oldpeak', 'thalach', 'exang', 'slope','ca','thal'],
                                       dtype='float',
                                       index=['input'])

        predictions = clf.predict(input_variables)[0]
        if predictions == 1:
            predictions = "Having Heart Disease"
        else :
            predictions = "Not Having heart disease"

        return render_template('heart.html', original_input={'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps,'chol':chol, 'fbs': fbs, 'restecg': restecg, 'oldpeak': oldpeak, 'thalach': thalach, 'exang': exang, 'slope': slope,'ca': ca, 'thal':thal},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)
