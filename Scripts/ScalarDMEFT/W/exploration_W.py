import csv
import subprocess
import numpy as np

# Para definir los parametros a manipular
param1 = 'MSDM'
param2 = 'W63'

# Para limpiar el output cada vez que se corra el script
with open('output_W.csv', 'w', newline='') as csvfile:
    pass 

# Para limpiar el data.par al principio
with open('/home/sgogoeg/heptools/micromegas_6.0/ScalarDMEFT/data.par', 'w') as tempfile:
    pass

# Leyendo el input
with open('input_W.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Corriendo sobre las filas del input
    for row in reader:
        # Escribiendo los parametros en el data1.par
        with open('/home/sgogoeg/heptools/micromegas_6.0/ScalarDMEFT/data.par', 'w') as tempfile:
            tempfile.write(f"{param1} {row[0]} \n{param2} {row[1]}\n")
        
        # Tomando el resultado
        result = subprocess.run(['./main', '/home/sgogoeg/heptools/micromegas_6.0/ScalarDMEFT/data.par'], cwd = "/home/sgogoeg/heptools/micromegas_6.0/ScalarDMEFT" ,stdout=subprocess.PIPE, text=True)

        # Variable para almacenar la densidad de reliquia
        omega_value = None

        # Abriendo el output
        with open('output_W.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Buscando el valor en cada lines
            for line in result.stdout.split('\n'):
                if "Omega=" in line:
                    omega_value = line.split("Omega=")[1] 
                    writer.writerow([row[0], row[1] ,omega_value])
                    break 