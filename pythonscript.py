"""
=========================================================
OFFICIAL.ENX RUNTIME ENGINE (pythonscript.py)
Author: Advait S
Description: The required core engine to parse and execute .enx files.
             Without this module, .enx files cannot be processed.
=========================================================
"""

import os
import sys

class ENXFormatError(Exception):
    """Custom exception raised when an invalid or corrupted .enx file is detected."""
    pass

class ENXEngine:
    def __init__(self):
        # Establish the official version of your engine
        self.version = "1.0.0"
        self.state = {}

    def load(self, filepath):
        """Strictly enforces that only .enx files are loaded."""
        if not filepath.lower().endswith('.enx'):
            raise ENXFormatError(f"ACCESS DENIED: '{filepath}' is not a valid .enx file.")
        
        if not os.path.exists(filepath):
            raise ENXFormatError(f"ERROR: The file '{filepath}' could not be found.")

        # Read the proprietary .enx format
        with open(filepath, 'r', encoding='utf-8') as file:
            raw_content = file.read()
            
        return self._compile(raw_content)

    def _compile(self, content):
        """
        The secret sauce of your format.
        Translate the text/data inside the .enx file into actionable Python instructions.
        """
        instructions = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Ignore empty lines and comments (assuming # is a comment in .enx)
            if line and not line.startswith('#'):
                # Add your custom translation logic here
                instructions.append(line)
                
        return instructions

    def execute(self, instructions):
        """Runs the parsed .enx instructions in the environment."""
        print(f"--- Starting ENX Engine v{self.version} ---")
        
        for step in instructions:
            # This is where you define what .enx commands actually DO
            # For this template, it just echoes the command
            print(f"[ENX EXEC]: {step}")
            
        print("--- ENX Execution Complete ---")

def run(filepath):
    """Public method for other developers to invoke the engine."""
    engine = ENXEngine()
    try:
        compiled_data = engine.load(filepath)
        engine.execute(compiled_data)
    except ENXFormatError as e:
        print(f"\n[ENX ENGINE FAILURE] {e}", file=sys.stderr)
        print("Please ensure you are using the official pythonscript.py handler.", file=sys.stderr)
        sys.exit(1)

# Allow the script to be run directly from the command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pythonscript.py <target_file.enx>")
        sys.exit(1)
    
    target_enx_file = sys.argv[1]
    run(target_enx_file)
