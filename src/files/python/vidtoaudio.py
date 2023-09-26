import os
import subprocess

import sys
def vitogiff(clipname, outputfile, formatt):
    if(formatt==".wav"):
        command = f'ffmpeg -y -i "{clipname}" -acodec pcm_s16le -ac 1 -ar 16000 "{outputfile}"'
    elif(formatt==".mp3"):
        command = f'ffmpeg -y -i "{clipname}" -acodec libmp3lame -ar 16000 "{outputfile}"'

    subprocess.run(command, shell=True)

if __name__ == "__main__":
    input_filename = sys.argv[1]  # Replace with your file name
    # output = sys.argv[2] 
    formatt= sys.argv[2] 
    directory, full_filename = os.path.split(input_filename)
    filename, extension = os.path.splitext(full_filename)
    output = directory+"/"+filename
    output= output+formatt

    vitogiff(input_filename, output, formatt)
