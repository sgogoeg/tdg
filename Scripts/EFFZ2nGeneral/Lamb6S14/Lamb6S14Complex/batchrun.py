'''
Corre exploration.py para todos los archivos dentro de la carpeta de inputs, los borra y genera un log file

Example:

python3 batchrun.py --micromegas-path /home/sgogoeg/heptools/micromegas_6.0

'''

import subprocess
import argparse
import glob
import os
from datetime import datetime

# Set up argument parser
parser = argparse.ArgumentParser(description='Run exploration.py on existing input files in the current directory, log the process, and delete input files upon successful completion.')
parser.add_argument('--micromegas-path', type=str, required=True, help='Path to the Micromegas directory')
args = parser.parse_args()

# Path to Micromegas
micromegas_path = args.micromegas_path

outputs_dir = "outputs"
os.makedirs(outputs_dir, exist_ok=True)

logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

# Find all input files in the inputs directory matching the pattern 'input_Z4_*.csv'
input_files = glob.glob(os.path.join('inputs', 'input_Z8_*.csv'))

# Open a log file to keep track of the process
log_date = datetime.now().strftime("%Y%m%d%H%M%S")  # Use YYYY-MM-DD format for the date
log_file_name = f"{log_date}_batchrun_log.txt"
log_file_path = os.path.join(logs_dir, log_file_name)
with open(log_file_path, 'w') as log_file:
    for input_file in input_files:
        # Generate corresponding output filename by replacing 'inputs/input_' with 'outputs/output_' in the input filename
        output_file = os.path.join(outputs_dir, 'output_' + os.path.basename(input_file).replace('input_', ''))
        
        # Log the start time in d/m/y H:M:S format
        start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_file.write(f"Start processing {input_file} at {start_time}\n")
        
        # Construct the command to run exploration.py
        command = ['python3', 'exploration.py', '--input', input_file, '--output', output_file, '--micromegas-path', micromegas_path]
        
        # Run exploration.py with subprocess.run
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Determine success or failure
        status = 'SUCCESS' if result.returncode == 0 else 'FAILURE'
        
        # Log the end time in d/m/y H:M:S format and status
        end_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_file.write(f"End processing {input_file} at {end_time}: {status}\n")
        
        # Delete the input file if processing was successful
        if result.returncode == 0:
            os.remove(input_file)
            log_file.write(f"Deleted {input_file} after successful processing.\n")
        else:
            log_file.write(f"Failed to process {input_file}, file not deleted.\n")

print("Process completed. Check", log_file_path, "for details.")
