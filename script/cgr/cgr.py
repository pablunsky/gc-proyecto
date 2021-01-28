# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 01:05:00 2021

@author: yogurtcongelado
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import array


class CGR:

    def __init__(self):
        # Iteraciones, afectan la calidad del dinujo
        self.iters = int(1e9)

        # Definicion de posiciones en el sistemas de coordenadas
        self.v1, self.v2, self.v3, self.v4 = [
            0., 0.], [0., 1.], [1., 0.], [1., 1.]

        # Transformacion de cadenas a sis de cc
        self.Proyector = {'A': self.v1, 'C': self.v2,
                          'T': self.v3, 'G': self.v4, }

    # Para poder operar con los fastas

    def read_fasta(self, content):
        L = ''
        for line in content.splitlines():
            if len(line) > 0 and line[0] != '>':
                for char in line:
                    if char != 'A' and char != 'T' and char != 'G' and char != 'C':
                        return None
                L += line.strip()
        return L

    # Ahora cargamos el nombre de un archivo

    def generate_gcr(self, content):
        h = self.read_fasta(content)

        if h == None:
            return None

        # Ahora realizamos el algoritmo con los datos trabajados
        conjunto = self.Juego_Caos_DNA(h, self.Proyector, len(h))

        x = conjunto[:, 0]
        y = conjunto[:, 1]

        heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

        plt.clf()
        plt.imshow(heatmap.T, extent=extent, origin='lower')
        plt.savefig('show_heat.png')

        plt.clf()
        plt.scatter(x, y, s=0.01)
        plt.savefig('show_scatter.png')

        plt.clf()
        plt.imshow(heatmap.T, extent=extent, origin='lower')
        plt.axis('off')
        plt.savefig('eval_heat.jpg', bbox_inches='tight')

        plt.close()

        return True

    def pmedio(self, t1, t2):
        x1, y1 = t1
        x2, y2 = t2
        z1 = (x1+x2)/2.0
        z2 = (y1+y2)/2.0
        return (z1, z2)

    def Juego_Caos_DNA(self, sec, coords, iters):
        P = [coords[sec[0]]]
        for i in range(iters):
            if i == self.iters:
                break
            vact = P[-1]
            pact = coords[sec[i]]
            psig = self.pmedio(vact, pact)
            P.append(psig)
        return array(P)
