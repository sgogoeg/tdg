'''

Genera N archivos con n puntos cada uno usando inputgenRandom y los guarda en una carpeta de inputs

Example:

python3 bachgen.py --files 5 --iterations 5
'''

import subprocess
import argparse
import os
import datetime


# Set up argument parser
parser = argparse.ArgumentParser(description='Run inputgenRandom.py N times with n iterations.')
parser.add_argument('--files', type=int, required=True, help='Number of times to run inputgenRandom.py')
parser.add_argument('--iterations', type=int, required=True, help='Number of iterations for each run')

args = parser.parse_args()

# Base name for output files
output_base_name = "input_Z4"

inputs_dir = "inputs"
os.makedirs(inputs_dir, exist_ok=True)

# Get the current date and format it as YYYYMMDD
today = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

for i in range(args.files):
    # Generate unique output filename for each run within the inputs directory, including the date
    output_filename = os.path.join(inputs_dir, f"{output_base_name}_{today}_{i}.csv")
    
    # Construct the command to run inputgenRandom.py
    command = ["python3", "inputgenRandom.py", "--output", output_filename, "--iterations", str(args.iterations)]
    
    # Run inputgenRandom.py with subprocess.run
    result = subprocess.run(command)
    
    # Check if the script ran successfully
    if result.returncode != 0:
        print(f"Error running {command}")
    else:
        print(f"Successfully generated {output_filename}")

print("All files generated.")
