from moviepy.editor import VideoFileClip
import sys
import os
def vitogiff(clipname, outputfile):
    # Load the video clip
    videoClip = VideoFileClip(clipname)

    videoClip.write_gif(outputfile, program="ffmpeg")

if __name__ == "__main__":
    input_filename = sys.argv[1]  # Replace with your file name
    
    directory, full_filename = os.path.split(input_filename)
    filename, extension = os.path.splitext(full_filename)
    output = directory+"/"+filename+".gif"
    vitogiff(input_filename, output)
