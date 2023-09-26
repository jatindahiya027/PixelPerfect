import os
import subprocess
import sys

def convert_to_wav(input_filename):
    # Check the file extension
    _, file_extension = os.path.splitext(input_filename)

    if file_extension.lower() != '.wav':
        # Convert to WAV using ffmpeg (you need to have ffmpeg installed)
        wav_filename = os.path.splitext(input_filename)[0] + '.wav'
        convert_command = f'ffmpeg -y -i "{input_filename}" "{wav_filename}"'
        subprocess.run(convert_command, shell=True)

        return wav_filename
    else:
        return input_filename

def vitogiff(clipname):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_directory)
    directory_path = os.path.dirname(clipname)
    command = f'deep-filter "{clipname}" -o "{directory_path}"'
    print(command)
    subprocess.run(command, shell=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input_filename")
        sys.exit(1)

    input_filename = sys.argv[1]

    # Convert to WAV if necessary and get the final filename
    wav_filename = convert_to_wav(input_filename)

    # Process the WAV file
    vitogiff(wav_filename)

    # Clean up the temporary WAV file if it was created
    # if wav_filename != input_filename:
    #     os.remove(wav_filename)

if __name__ == "__main__":
    main()
