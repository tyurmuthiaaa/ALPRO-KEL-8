import numpy as np
import pickle
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediksi/', methods=['GET','POST'])
def prediksi():
    if request.method =='GET':
        return render_template('prediksi.html')
    else:
        features = [int(i) for i in request.form.values()]
        array_features = [np.array(features)]
        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(array_features)
        output = prediction

        # Check the output values and retrive the result with html tag based on the value
        if output == 1:
            result='Anda berpotensi terkena penyakit kolesterol!'
            result2='Disarankan untuk melakukan pemeriksaan pada dokter dan yuk cek pola hidup sehat yang cocok untukmu!'
        else:
            result='Anda tidak berpotensi terkena penyakit kolesterol!'
            result2='ets! jangan sampai lengah, yuk cek pola hidup sehat rekomendasi kami!'
    return render_template('prediksi.html', result=result,result2 = result2)

@app.route('/polamakan/')
def polamakan():
    return render_template('polamakan.html')

@app.route('/polamakan1/')
def polamakan1():
    return render_template('polamakan1.html')

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)