'''
El script genera un archivo csv con la reticula en el espacio de parametros entre los rangos de masas y acoples especificados

Se toma un espaciado logaritmico en el espacio de parametros

El Script toma como input el nombre del output y el numero de iteraciones (puntos)

Example:

python3 inputgen.py --output input.csv --pointsM1 100 --pointsM4 5 --pointsCoupling 100 --minM1 1 --maxM1 1000 --minM4 1 --maxM4 1000 --minCoupling 0.01 --maxCoupling 1 --files 10

'''

import argparse
import csv
import numpy as np
import os
import datetime

parser = argparse.ArgumentParser(description='Generates desired parameter space.')

parser.add_argument('--output', type=str, required=True, help='Path to the output CSV file')

parser.add_argument('--pointsM1', type=int, default=1000, help='Number of points in M1')
parser.add_argument('--pointsM4', type=int, default=1000, help='Number of points in M4')
parser.add_argument('--pointsCoupling', type=int, default=1000, help='Number of points in the desired coupling')

parser.add_argument('--minM1', type=float, default=1, help='Lower limit on M1 in GeV')
parser.add_argument('--maxM1', type=float, default=1000, help='Upper limit on M1 in GeV')
parser.add_argument('--minM4', type=float, default=1, help='Lower limit on M1 in GeV')
parser.add_argument('--maxM4', type=float, default=1000, help='Upper limit on M1 in GeV')
parser.add_argument('--minCoupling', type=float, default=1, help='Lower limit on Coupling')
parser.add_argument('--maxCoupling', type=float, default=1000, help='Upper limit on Coupling')

parser.add_argument('--files', type=int, required=True, help='Number of files to split output')

args = parser.parse_args()

# Parametros generales del espaciado

base = 10

# Masa campo 1


M1 = np.logspace(np.log10(args.minM1), np.log10(args.maxM1), args.pointsM1, base=base)

# Masa campo 4

M4 = np.logspace(np.log10(args.minM4), np.log10(args.maxM4), args.pointsM4, base=base)

# muS1

coupling = np.logspace(np.log10(args.minCoupling), np.log10(args.maxCoupling), args.pointsCoupling, base=base)

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
DMdelSA = 0
DMdelSB = 1e-5
DMdelAB = 0


input = []

for m1 in M1:
    for m4 in M4:
        for c in coupling:
            DMdelSA = c
            input_temp = np.array([m1, DMlamb41, m4, DMlamb44, DMlamb414, DMlambS1, DMlambS4, DMlamb6141, DMlamb6142, DMlambS41, 
                                   DMlambS21, DMlambS44, DMlambS24, DMlamb6S14, DMlambE8, DMdelSA, DMdelSB, DMdelAB])
            input.append(input_temp)

# Convirtiendo en un solo array de numpy y guardando

input = np.vstack(input)

np.savetxt(f'inputs/{args.output}', input, delimiter=",")

# Ahora el splitting del output

def split_csv(input_file, n):
    # Open the input CSV file
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        
        # Read the header row
        #header = next(reader)
        
        # Calculate the number of rows per new file
        total_rows = sum(1 for _ in reader)
        rows_per_file = total_rows // n
        
        # Reset the file pointer to the beginning
        infile.seek(0)
        next(reader)  # Skip the header again

        # Get the current date and format it as YYYYMMDD
        today = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Create and write to new CSV files
        for i in range(n):
            with open(f"{input_file[:-4]}_Z8_{today}_part_{i}.csv", 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                
                # Write the header row
                #writer.writerow(header)
                
                # Write rows for this file
                for _ in range(rows_per_file):
                    try:
                        writer.writerow(next(reader))
                    except StopIteration:
                        break
                
                # Write remaining rows for the last file
                if i == n - 1:
                    writer.writerows(reader)
    # Delete the original file
    try:
        os.remove(input_file)
    except OSError as e:
        print(f"Error deleting original file '{input_file}': {e}")

split_csv(f'inputs/{args.output}', args.files)
