from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from coffee_cnn_Classifier.utils import decodeImage
from coffee_cnn_Classifier.pipeline.predict import HemileiaVastatrix


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = HemileiaVastatrix(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

