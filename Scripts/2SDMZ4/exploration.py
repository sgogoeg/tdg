import csv
import subprocess
import numpy as np

# Para definir los parametros a manipular
param1 = 'MDM1'
param2 = 'DMlamb41'
param3 = 'MDM2'
param4 = 'DMlamb42'
param5 = 'DMlamb412'
param6 = 'DMlambS1'
param7 = 'DMlambS2'
param8 = 'DMmuS1'
param9 = 'DMlamb51'

# Para limpiar el output cada vez que se corra el script
with open('output_Z4.csv', 'w', newline='') as csvfile:
    pass 

# Para limpiar el data.par al principio
with open('/home/sgogoeg/heptools/micromegas_6.0/Z42SDM/data.par', 'w') as tempfile:
    pass

# Leyendo el input
with open('input_Z4.csv', 'r') as csvfile:
    
    # Escribiendo los nombres de las variables en el CSV

    writer = csv.writer(csvfile)

    writer.writerow([param1, param2, param3, param4, param5, param6, param7, param8, param9, "omega1", "omega2", "omegaFI"])
    
    reader = csv.reader(csvfile)

    # Corriendo sobre las filas del input
    for row in reader:
        # Escribiendo los parametros en el data1.par
        with open('/home/sgogoeg/heptools/micromegas_6.0/Z42SDM/data.par', 'w') as tempfile:
            tempfile.write(f"{param1} {row[0]}\n {param2} {row[1]}\n {param3} {row[2]}\n {param4} {row[3]}\n {param5} {row[4]}\n {param6} {row[5]}\n {param7} {row[6]}\n {param8} {row[7]}\n {param9} {row[8]}\n")
        
        # Tomando el resultado
        result = subprocess.run(['./main', '/home/sgogoeg/heptools/micromegas_6.0/Z42SDM/data.par'], cwd = "/home/sgogoeg/heptools/micromegas_6.0/Z42SDM" ,stdout=subprocess.PIPE, text=True)

        # Variable para almacenar la densidad de reliquia
        omega_value_1 = None
        omega_value_2 = None
        omega_value_FI = None

        # Abriendo el output
        with open('output_Z4.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Buscando los valores en cada linea
            for line in result.stdout.split('\n'):
                if "Omega1 (N)=" in line:
                    omega_value_1 = line.split("Omega1 (N)=")[1] 

                if "Omega2 (N)=" in line:
                    omega_value_2 = line.split("Omega2 (N)=")[1] 
        
                if "Omega_FI=" in line:
                    omega_value_FI = line.split("Omega_FI=")[1] 
                    writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], omega_value_1, omega_value_2, omega_value_FI])
                    break
                
                # Si no encuentra nada debe escribir algo

                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], omega_value_1, omega_value_2, omega_value_FI])