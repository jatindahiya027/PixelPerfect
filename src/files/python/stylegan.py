import subprocess
import random
import sys
import os
# Generate a random 6-digit number for the seed
random_seed = random.randint(100000, 999999)
script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)
# Define the command as a list of arguments, including the random seed
mode = sys.argv[2]
if mode=="0":
 command = [
    "python",
    "./stylegan3-cpu/gen_images.py",
    f"--outdir={sys.argv[1]}",
    "--trunc=0.8",
    f"--seeds={random_seed}",
    "--cols=1",
    "--network=https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-t-ffhq-1024x1024.pkl"
]
elif mode=="1":
 command = [
    "python",
    "./stylegan3-cpu/gen_images.py",
     f"--outdir={sys.argv[1]}",
    "--trunc=0.7",
    f"--seeds={random_seed}",
    "--cols=1",
    "--network=stylegan_human_v3_512.pkl"
]
# Run the command
try:
    subprocess.run(command, check=True)
    print(f"Command executed successfully with random seed: {random_seed}")
except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")
except FileNotFoundError as e:
    print(f"Command not found: {e}")
