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

M4 = M1

# LambS41

StartCoup = np.log10(1e-9)
StopCoup = np.log10(1e-4)

S41 = np.logspace(StartCoup, StopCoup, num_samples, base=base)
S44 = np.logspace(StartCoup, StopCoup, num_samples, base=base)



# Inicializando el input de salida

DMlamb41 = 0
DMlamb44 = 0 
DMlamb414 = 0
DMlambS1 = 0
DMlambS4 = 0
DMlamb6141 = 0
DMlamb6142 = 0
DMlambS41 = 0
DMlambS21 = 0
DMlambS44 = 0
DMlambS24 = 0 
DMlamb6S14 = 0
DMlambE8 = 0


input = []

i = 0

while i < args.iterations:
    randinx = np.random.randint(0, num_samples, 4)
    m1 = M1[randinx[0]]
    m4 = M4[randinx[1]]
    DMlambS41 = S41[randinx[2]]
    DMlambS44 = S44[randinx[3]]
    input_temp = np.array([m1, DMlamb41, m4, DMlamb44, DMlamb414, DMlambS1, DMlambS4, DMlamb6141, DMlamb6142, DMlambS41, DMlambS21, DMlambS44, DMlambS24, DMlamb6S14, DMlambE8])
    input.append(input_temp)
    i += 1

# Convirtiendo en un solo array de numpy y guardando

input = np.vstack(input)

np.savetxt(args.output, input, delimiter=",")

