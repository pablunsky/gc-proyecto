import base64
import csv
import json
from datetime import datetime

import cv2
import numpy as np
from flask import Flask, render_template, request, url_for
from PIL import Image
import io
from script.cgr.cgr import CGR

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('site/home.html')


@app.route('/uploadFile', methods=['POST'])
def upload_fasta():
    data = request.get_json()
    content = base64.b64decode(data['data']).decode('utf-8')

    graph = CGR()
    graph.generate_gcr(content)

    heatmap = open('testplot_heat.png', 'rb')
    base64_heat = base64.b64encode(heatmap.read())

    scatter = open('testplot_scatter.png', 'rb')
    base64_scatter = base64.b64encode(scatter.read())

    return {'status': 'OK', 'heat': str(base64_heat), 'scatter': str(base64_scatter)}


if __name__ == '__main__':
    app.run(port=5000, debug=True)
