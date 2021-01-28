import base64
import csv
import io
import json
from datetime import datetime

import cv2
import numpy as np
from flask import Flask, render_template, request, url_for
from PIL import Image

from script.cgr.cgr import CGR
from script.regression.regression import evaluate

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('site/home.html')


@app.route('/uploadFile', methods=['POST'])
def upload_fasta():
    data = request.get_json()
    content = base64.b64decode(data['data']).decode('utf-8')

    graph = CGR()
    result = graph.generate_gcr(content)
    if result == None:
        return {'status': 'NOTOK'}

    heatmap = open('show_heat.png', 'rb')
    base64_heat = base64.b64encode(heatmap.read())

    scatter = open('show_scatter.png', 'rb')
    base64_scatter = base64.b64encode(scatter.read())

    addr = "eval_heat.jpg"
    img = cv2.imread(addr)
    img = cv2.resize(img, (389, 389), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    data = np.array(img[None])
    data = data.reshape(data.shape[0], -1).T
    data = np.append([1], data)

    result = "No se pudo determinar un tipo de virus."
    if evaluate('modelos.chikungunya1', data) == 0:
        result = "Se ha determinado un genoma de Chikungunya."
    elif evaluate('modelos.zika1', data) == 0:
        result = "Se ha determinado un genoma de Zika."
    elif evaluate('modelos.dengue1', data) == 0:
        result = "Se ha determinado un genoma de Dengue."

    return {'status': 'OK', 'heat': str(base64_heat), 'scatter': str(base64_scatter), 'result': result}


if __name__ == '__main__':
    app.run(port=5000, debug=True)
