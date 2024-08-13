'''
El script genera un archivo csv con puntos seleccionados al azar dentro de un espacio de parametros especificado

Se toma un espaciado logaritmico en el espacio de parametros

Tratamos el caso de masa 2 menor a masa 1

'''

import numpy as np

# Parametros que siempre son cero

lamb51 = 0

lamb41 = 0

lamb42 = 0

# Parametros generales del espaciado

iter = 1000
num_samples = 10000
base = 10

# Masa campo 1

startM1 = np.log10(40)
stopM1 =  np.log10(2000)

M1 = np.logspace(startM1, stopM1, num_samples, base=base)

# Masa campo 2

M2 = np.logspace(startM1, stopM1, num_samples, base=base)

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

startmuS1 = 2
stopmuS1 =  4

muS1 = np.logspace(startmuS1, stopmuS1, num_samples, base=base)

# Inicializando el input de salida

input = []

Mh = 125

vev = 246

i = 0

while(i<iter):
    randinx = np.random.randint(0, num_samples, 6)
    paramtemp = np.array([M1[randinx[0]], lamb41, M2[randinx[1]], lamb42, lamb412[randinx[2]], lambS1[randinx[3]], lambS2[randinx[4]],
                     muS1[randinx[5]], lamb51])

    Gamma1 = (paramtemp[0]<(Mh/2)) * 2 * paramtemp[5]**2 * vev**2 /(32*np.pi*Mh) * np.sqrt(1 - 4*paramtemp[0]**2/Mh**2 + 0j)

    Gamma2 = (paramtemp[2]<(Mh/2)) * paramtemp[6]**2 * vev**2 /(32*np.pi*Mh) * np.sqrt(1 - 4*paramtemp[2]**2/Mh**2 + 0j)

    # Condiciones para acoples no imaginarios y herarquias de masas
    if (paramtemp[0] > paramtemp[2]) and ((paramtemp[0]**2 - 1/2 * paramtemp[5] * 246**2) > 0) and ((paramtemp[2]**2 - 1/2 * paramtemp[6] * 246**2) > 0) and (paramtemp[2] < 2*paramtemp[0]) and ((Gamma1 + Gamma2)/4.1e-3  <= 0.13):
        input.append(paramtemp)
        i += 1

# Convirtiendo en un solo array de numpy y guardando

input = np.vstack(input)

np.savetxt("input_Z4.csv", input, delimiter=",")
