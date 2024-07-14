'''
El script genera un archivo csv con puntos de un benchmark point dentro de un espacio de parametros especificado.

Seleccionamos un benchmark point de M2 = 10^3 y muS1 > 10^3.

Se toma un espaciado logaritmico en el espacio de parametros.

Tratamos el caso de masa 2 menor a masa 1.

'''

import numpy as np

param8 = 'DMmuS1'

# Parametros que siempre son cero

lamb51 = 0

lamb41 = 0

lamb42 = 0

# Parametros generales del espaciado

num_samples = 7
base = 10

# Masa campo 1

startM1 = 3
stopM1 =  4

M1 = np.logspace(startM1, stopM1, num_samples, base=base)

# Masa campo 2 (Depende de la masa del campo 1)

m2 = 1e3

# LambdaS1

startlambS1 = -4
stoplambS1 =  0

lambS1 = np.logspace(startlambS1, stoplambS1, num_samples, base=base)

# LambdaS2

startlambS2 = -4
stoplambS2 =  0

lambS2 = np.logspace(startlambS2, stoplambS2, num_samples, base=base)

# Lambda412

startlamb412 = -4
stoplamb412 =  0

lamb412 = np.logspace(startlamb412, stoplamb412, num_samples, base=base)

# muS1

startmuS1 = 3
stopmuS1 =  4

muS1 = np.logspace(startmuS1, stopmuS1, num_samples, base=base)

input = []

# Iterando sobre los diferentes arreglos
for m1 in M1:
    for ls1 in lambS1:
        for ls2 in lambS2:
            for l412 in lamb412:
                for mu in muS1:
                    input_temp = np.array([m1, lamb41, m2, lamb42, l412, ls1, ls2, mu, lamb51])
                    input.append(input_temp)

# Convirtiendo en un unico arreglo de numpy
input = np.vstack(input)

# Guardando a csv
np.savetxt("input_Z4.csv", input, delimiter=",")
