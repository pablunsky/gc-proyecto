import numpy as np
import cv2
from script.regression.regression import generate_model, get_models
import sys

generate_model('data/zika.hdf5',
               'Zika', False, int(sys.argv[1]), 'modelos.zika', False)

addr = "zika.jpg"
img = cv2.imread(addr)
img = cv2.resize(img, (389, 389), interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
data = np.array(img[None])
data = data.reshape(data.shape[0], -1).T
data = np.append([1], data)

chikungunya, dengue, zika = get_models()

result = chikungunya[0].predict(data)
print(result)

result = dengue[0].predict(data)
print(result)

result = zika[0].predict(data)
print(result)
