#!/usr/bin/python
from subprocess import Popen
import sys

# Get the target script filename from the command-line arguments
filename = sys.argv[1]

# Continuously loop to restart the script whenever it crashes or exits
while True:
    print("\nStarting " + filename)
    
    # Run the specified Python script in a separate shell process
    p = Popen("python " + filename, shell=True)  # Restarts remotorX_XX.py when an error occurs
    
    # Wait for the process to finish before looping back to restart it
    p.wait()
