'''
Este script corre un comando en un numero dado de instancias. El comando va al fondo a través de nohup &

Debe especificarse la ultima instancia que debe tomarse. En este caso esta limitado a 15 instancias

e.g:

python3 parallel.py --end-number 2 --command "python3 bachgen.py --files 5 --iterations 5"

python3 parallel.py --end-number 2 --command "python3 batchrun.py --micromegas-path /home/sgogoeg/heptools/micromegas_6.0"

'''

import subprocess
import argparse
import os

def run_command(original_directory, directory, command):
    try:
        # Save the original directory
        original_directory = os.getcwd()
        
        # Change the current working directory
        os.chdir(directory)
        
        # Prepend 'nohup' and append '&' to the command to run it in the background
        nohup_command = f"nohup {command} &"
        
        # Execute the command
        result = subprocess.run(nohup_command, shell=True, capture_output=False, text=False)
        
        # Print the output
        print(f"Started {command} in the background for {directory}. Output saved to output_{directory}.txt")
        
    finally:
        # Revert back to the original directory
        os.chdir(original_directory)

def run_commands(start_number, end_number, command):
    for n in range(start_number, end_number+1):
        # Construct the directory path, replacing {n} with the actual number
        directory = os.path.join(".", f"instance{n}")  # Using "." for the current directory
        run_command(os.getcwd(), directory, command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change directories and run commands on the host machine.")
    parser.add_argument("--end-number", type=int, required=True, help="Ending number for directories.")
    parser.add_argument("--command", type=str, required=True, help="Command to run in each instance directory.")

    args = parser.parse_args()

    start_number = 0
    end_number = args.end_number
    command = args.command
    
    run_commands(start_number, end_number, command)
