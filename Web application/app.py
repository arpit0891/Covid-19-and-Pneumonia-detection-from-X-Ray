from flask import Flask, render_template, request, send_from_directory
import cv2
import tensorflow as tf
from tensorflow import keras
import h5py
import numpy as np
COUNT = 0
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1
loaded_model = keras.models.load_model('covid19.h5')
@app.route('/')
def man():
    return render_template('index.html')
@app.route('/home',methods=['post', 'get'])
def home():
    global COUNT
    img = request.files['image']
    img.save('static/{}.jpg'.format(COUNT))    
    img = cv2.imread('static/{}.jpg'.format(COUNT))
    img = cv2.resize(img,(224,224))
    img = np.reshape(img,[1,224,224,3])
    classes = loaded_model.predict_classes(img)
    COUNT+=1
    d=['BacterialPneumonia', 'COVID-19','Normal','ViralPneumonia']
    return render_template('prediction.html', data=d[classes[0]])
@app.route('/load_img')
def load_img():
    global COUNT
    return send_from_directory('static', "{}.jpg".format(COUNT-1))


if __name__ == '__main__':
    app.run(debug=True)