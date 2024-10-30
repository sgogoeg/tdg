'''
El script genera un archivo csv con la reticula en el espacio de parametros entre los rangos de masas y acoples especificados

Se toma un espaciado logaritmico en el espacio de parametros

El Script toma como input el nombre del output y el numero de iteraciones (puntos)

Example:

python3 inputgenRandom.py --output input.csv --iterations 5000

'''

import argparse
import csv
import numpy as np
import os
import datetime

parser = argparse.ArgumentParser(description='Generates desired parameter space.')
parser.add_argument('--output', type=str, required=True, help='Path to the output CSV file')
parser.add_argument('--iterations', type=int, default=1000, help='Number of iterations')
args = parser.parse_args()

# Parametros generales del espaciado

base = 10
num_samples = 10000

iter = args.iterations  # Using the number of iterations from arguments

startM = np.log10(1)
stopM =  np.log10(2000)

# Masa campo complejo

M1 = np.logspace(startM, stopM, num_samples, base=base)

# Masa campo real

M5 = M1

# LambS41

StartCoup = np.log10(1e-9)
StopCoup = np.log10(1e-4)

S41 = np.logspace(StartCoup, StopCoup, num_samples, base=base)
S45 = np.logspace(StartCoup, StopCoup, num_samples, base=base)



# Inicializando el input de salida

DMlamb41 = 0
DMlamb45 = 0 
DMlamb415 = 0
DMlambS1 = 0
DMlambS5 = 0
DMlamb6151 = 0
DMlamb6152 = 0
DMlambS41 = 0
DMlambS21 = 0
DMlambS45 = 0
DMlambS25 = 0 
DMlamb6S15 = 0
DMlambE10 = 1


input = []

i = 0

while i < args.iterations:
    randinx = np.random.randint(0, num_samples, 4)
    m1 = M1[randinx[0]]
    m5 = M5[randinx[1]]
    DMlambS41 = S41[randinx[2]]
    DMlambS45 = S45[randinx[3]]
    input_temp = np.array([m1, DMlamb41, m5, DMlamb45, DMlamb415, DMlambS1, DMlambS5, DMlamb6151, DMlamb6152, DMlambS41, DMlambS21, DMlambS45, DMlambS25, DMlamb6S15, DMlambE10])
    input.append(input_temp)
    i += 1

# Convirtiendo en un solo array de numpy y guardando

input = np.vstack(input)

np.savetxt(args.output, input, delimiter=",")

