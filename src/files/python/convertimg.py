import os
import concurrent.futures
# from PIL import Image
import time
import subprocess
import sys
import json
def convert_image(input_path,outpath,ico):

    cmd = f'convert "{input_path}" "{outpath}"'
    if ico==".ico":
     cmd = f'convert "{input_path}" -resize 72x72 "{outpath}"'
    
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except FileNotFoundError:
        print("The 'transparent-background' command was not found. Make sure it's installed and in your PATH.")


def main():
    image_files = json.loads(sys.argv[1])

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for img_file in image_files:
            input_path =  img_file
            outpath, test =os.path.splitext(input_path)
            # print(outpath)
            outpath= outpath+sys.argv[2]
            # outpath = os.path.join(directory_name, file_name+sys.argv[1])
            # output_path = os.path.join(output_folder, img_file)
            future = executor.submit(convert_image, input_path,outpath ,sys.argv[2])
            futures.append(future)
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
