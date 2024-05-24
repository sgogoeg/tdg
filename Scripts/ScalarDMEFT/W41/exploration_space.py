import csv
import subprocess
import numpy as np

vev = 246.22

# Para definir los parametros a manipular
param1 = 'MSDM'
param2 = 'W41'

def mu(MSDM,C):
    return np.sqrt(MSDM**2 - 1/2 * C * vev**2)

# Para limpiar el output cada vez que se corra el script
with open('output.csv', 'w', newline='') as csvfile:
    pass 

# Para limpiar el data.par al principio
with open('data.par', 'w') as tempfile:
    pass

# Leyendo el input
with open('inputspace.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Corriendo sobre las filas del input
    for row in reader:
        # Escribiendo los parametros en el data1.par
        with open('data.par', 'w') as tempfile:
            tempfile.write(f"{param1} {row[0]} \n{param2} {row[1]}\n")
        
        # Tomando el resultado
        result = subprocess.run(['./main', 'data.par'], stdout=subprocess.PIPE, text=True)

        # Variable para almacenar la densidad de reliquia
        omega_value = None

        # Abriendo el output
        with open('outputspace.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Buscando el valor en cada lines
            for line in result.stdout.split('\n'):
                if "Omega=" in line:
                    omega_value = line.split("Omega=")[1] 
                    writer.writerow([row[0], row[1] ,omega_value])
                    break 