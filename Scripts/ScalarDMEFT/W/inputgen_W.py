'''
El script genera un archivo csv con puntos seleccionados dentro de un espacio de parámetros especificado

Se toma un espaciado logaritmico en el espacio de parámetros

'''

import numpy as np

# Número de puntos dentro del intervalo 

num_samples = 320

# Coeficiente

startcoup = -8
stopcoup =  -5
basecoup = 10 

couplings = np.logspace(startcoup, stopcoup, num_samples, base=basecoup)

# Masa

startmass = 0
stopmass =  3
basemass = 10 

masses = np.logspace(startmass, stopmass, num_samples, base=basemass)

input = []

for i in masses:

    mass = i*np.ones(couplings.shape)
    inputtemp = np.column_stack((mass, couplings))

    input.append(inputtemp)

input = np.vstack(input)

# Guardando a csv
np.savetxt("input_W.csv", input, delimiter=",")