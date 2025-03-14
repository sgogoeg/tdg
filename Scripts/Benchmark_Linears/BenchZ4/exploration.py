'''
El script toma un archivo csv como input para correr micromegas con los parámetros especificados.

El nombre del modelo de micromegas debe cambiarse.

El camino de micromegas, el nombre del input file y el nombre del output file son parametros del script

Example:

python3 exploration.py --input input_Z4.csv --output output_Z4.csv --micromegas-path /home/sgogoeg/heptools/micromegas_6.0

'''

import argparse
import csv
import subprocess

# Set up argument parser
parser = argparse.ArgumentParser(description='Run Micromegas with specified parameters.')
parser.add_argument('--input', type=str, required=True, help='Path to the input CSV file')
parser.add_argument('--output', type=str, required=True, help='Path to the output CSV file')
parser.add_argument('--micromegas-path', type=str, required=True, help='Path to the Micromegas directory')

args = parser.parse_args()

# Para definir los parametros a manipular, debe corresponder con los nombres y el orden de los parámetros en el modelo entregado a micrOmegas
params = ['MDM1', 'DMlamb41', 'MDM2', 'DMlamb42', 'DMlamb412', 'DMlambS1', 'DMlambS2', 'DMmuS1', 'DMlamb51'] 

# Para limpiar el data.par al principio
data_par_path = f'{args.micromegas_path}/Z42SDM/data0.par'
with open(data_par_path, 'w') as tempfile:
    pass

# Leyendo el input
with open(args.input, 'r') as csvfile:
    
    # Escribiendo los nombres de las variables en el CSV
    
    reader = csv.reader(csvfile)

    # Corriendo sobre las filas del input
    for row in reader:
        # Escribiendo los parametros en el data1.par
        with open(data_par_path, 'w') as tempfile:
            tempfile.write(f"{params[0]} {row[0]}\n {params[1]} {row[1]}\n {params[2]} {row[2]}\n {params[3]} {row[3]}\n {params[4]} {row[4]}\n {params[5]} {row[5]}\n {params[6]} {row[6]}\n {params[7]} {row[7]}\n {params[8]} {row[8]}\n")
        
        # Tomando el resultado
        result = subprocess.run(['./main', data_par_path], cwd=f'{args.micromegas_path}/Z42SDM/' ,stdout=subprocess.PIPE, text=True)

        # Variable para almacenar la densidad de reliquia
        omega_value_1 = None
        omega_value_2 = None
        omega_value_Tot = None

        # Abriendo el output
        with open(args.output, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Buscando los valores en cada linea
            for line in result.stdout.split('\n'):
                parts = line.split()  # Separando por espacios
                for part in parts:
                    if "Omega_1h^2=" in part:
                        omega_value_1 = part.split("Omega_1h^2=")[1]
                    elif "Omega_2h^2=" in part:
                        omega_value_2 = part.split("Omega_2h^2=")[1]
            if omega_value_1 and omega_value_2:
                omega_value_Tot = float(omega_value_1) + float(omega_value_2)
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], omega_value_1, omega_value_2, omega_value_Tot])
                
                # Si no encuentra nada debe escribir algo
            else:
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], 0, 0, 0])