import os
import subprocess

import sys
def vitogiff(clipname, type, directory_path):
    # 3.jpg --type rgba
    os.chdir(directory_path)
    command = f'transparent-background --source "{clipname}" --type "{type}"'
   

    subprocess.run(command, shell=True)

if __name__ == "__main__":
    input_filename = sys.argv[1]  # Replace with your file name
    type= sys.argv[2] 
    directory_path = os.path.dirname(input_filename)
    vitogiff(input_filename, type,directory_path)
