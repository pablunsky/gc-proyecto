import pickle
from script.regression.data import Data
from script.regression.model import Model
import script.regression.plotter as Plotter
import csv
import numpy as np
import h5py


def load_dataset(dataset, tag):
    dataset = h5py.File(dataset, "r")

    # entradas de entrenamiento
    train_set_x_orig = np.array(dataset["train_img"][:])
    # salidas de entrenamiento
    train_set_y_orig = np.array(dataset["train_labels"][:])

    test_set_x_orig = np.array(dataset["test_img"][:])  # entradas de prueba
    test_set_y_orig = np.array(dataset["test_labels"][:])  # salidas de prueba

    # Les aplica reshape, convierte al arreglo en un arreglo de areglos
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, [tag, 'Otro']


def generate_model(dataset, tag, ONLY_SHOW, index, binary_file, read):

    if read:
        with open(binary_file, 'rb') as f:
            models = pickle.load(f)
            Plotter.show_Model(models)
        exit()

    # Cargando conjuntos de datos
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset(
        dataset, tag)

    if ONLY_SHOW:
        Plotter.show_picture(train_set_x_orig[index])
        print(classes[train_set_y[0][index]])
        exit()

    # Convertir imagenes a un solo arreglo
    train_set_x = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
    test_set_x = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

    print('Original: ', train_set_x_orig.shape)
    print('Con reshape: ', train_set_x.shape)

    # Conjuntos de datos
    train_set = Data(train_set_x, train_set_y, 255)
    test_set = Data(test_set_x, test_set_y, 255)

    model1 = Model(train_set, test_set, reg=False, alpha=0.0001, lam=0)
    model1.training()

    #model2 = Model(train_set, test_set, reg=True, alpha=0.0001, lam=150)
    # model2.training()

    #model3 = Model(train_set, test_set, reg=False, alpha=0.001, lam=0)
    # model3.training()

    # model4 = Model(train_set, test_set, reg=True, alpha=0.001,
    #               lam=150)
    # model4.training()

    #model5 = Model(train_set, test_set, reg=True, alpha=0.001, lam=200)
    # model5.training()

    # models = [model1, model3]  # , model3, model4, model5]
    # Plotter.show_Model(models)

    with open(binary_file, 'wb') as f:
        pickle.dump(model1, f)


# generate_model('DataFactory/datasets/ufm.hdf5',
#               'UFM', False, 0, 'modelos.ufm', True)

# generate_model('DataFactory/datasets/url.hdf5',
#               'URL', False, 4, 'modelos.url', True)

# generate_model('DataFactory/datasets/umg.hdf5',
#               'UMG', False, 4, 'modelos.umg', True)


def evaluate(file, data):
    models = None

    with open(file, 'rb') as f:
        models = pickle.load(f)

    return models.predict(data)
