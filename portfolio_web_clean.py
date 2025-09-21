import sys
import os
import logging
import subprocess
from dotenv import load_dotenv

# Suppress all logging
logging.getLogger().setLevel(logging.CRITICAL)

def main():
    """
    Generate clean portfolio data starting from "--- Consolidated Portfolio ---"
    """
    # Run the portfolio script and capture output
    result = subprocess.run([
        'python3', 'portfolio_app.py'
    ], capture_output=True, text=True, cwd='/home/ubuntu/PORTFOLIO')
    
    # Find the start of the portfolio section
    output_lines = result.stdout.split('\n')
    portfolio_start = -1
    
    for i, line in enumerate(output_lines):
        if "--- Consolidated Portfolio ---" in line:
            portfolio_start = i
            break
    
    if portfolio_start >= 0:
        # Print only from the portfolio section onwards
        for line in output_lines[portfolio_start:]:
            print(line)
    else:
        print("Error: Could not find portfolio section in output")

if __name__ == '__main__':
    main()
