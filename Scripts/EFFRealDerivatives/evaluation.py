'''
El script toma un archivo csv como input para correr micromegas con los parámetros especificados.

La dirección y el nombre del modelo de micrOmegas es sensible a las diferentes maquinas
'''

import csv
import subprocess
import numpy as np

# Para definir los parametros a manipular, debe corresponder con los nombres y el orden de los parámetros en el modelo entregado a micrOmegas
param1 = 'MSDM'
param2 = 'WLap'

# Para limpiar el output cada vez que se corra el script
with open('output.csv', 'w', newline='') as csvfile:
    pass 

# Para limpiar el data.par al principio
with open('/home/sgogoeg/heptools/micromegas_6.0/EFFRealDerivatives/data.par', 'w') as tempfile:
    pass

# Leyendo el input
with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Corriendo sobre las filas del input
    for row in reader:
        # Escribiendo los parametros en el data1.par
        with open('/home/sgogoeg/heptools/micromegas_6.0/EFFRealDerivatives/data.par', 'w') as tempfile:
            tempfile.write(f"{param1} {row[0]} \n{param2} {row[1]}\n")
        
        # Tomando el resultado
        result = subprocess.run(['./main', '/home/sgogoeg/heptools/micromegas_6.0/EFFRealDerivatives/data.par'], cwd = "/home/sgogoeg/heptools/micromegas_6.0/EFFRealDerivatives" ,stdout=subprocess.PIPE, text=True)

        # Variable para almacenar la densidad de reliquia
        omega_value = None

        # Abriendo el output
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Buscando el valor en cada lines
            for line in result.stdout.split('\n'):
                if "Omega=" in line:
                    omega_value = line.split("Omega=")[1] 
                    writer.writerow([row[0], row[1] ,omega_value])
                    break 
