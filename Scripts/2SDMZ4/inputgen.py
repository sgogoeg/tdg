import numpy as np

# Primero el caso de masa 2 menor a masa 1

param8 = 'DMmuS1'

# siempre es cero

lamb51 = 0

lamb41 = 0

lamb42 = 0

# Parametros generales

num_samples = 100
base = 10

# Masa campo 1

startM1 = 1
stopM1 =  4

M1 = np.logspace(startM1, stopM1, num_samples, base=base)

# Masa campo 2 (Depende de la masa del campo 1)

# La condicion masa 2 < 2 masa 1 se alcanza al subir el order en 1 y buscando hasta el doble

M2 = np.logspace(startM1, stopM1+1, num_samples, base=base)

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



input = []

for i in masses:

    mass = i*np.ones(couplings.shape)
    inputtemp = np.column_stack((mass, couplings))

    input.append(inputtemp)

input = np.vstack(input)

# Save to CSV
np.savetxt("input_Z4.csv", input, delimiter=",")