import os
import concurrent.futures
# from PIL import Image
import time
import subprocess
import sys
import json

MAX_RETRIES = 20  # Maximum number of times to retry the conversion

def convert_image(input_path, outpath, format, depth, quality):
    retries = 0
    while retries < MAX_RETRIES:
        if format == ".tif":
            cmd = f'convert "{input_path}" -compress ZIP "{outpath}"'
        elif format == ".png":
            cmd = f'convert "{input_path}" -depth {depth} -compress Zip "{outpath}"'
        else:
            cmd = f'convert "{input_path}" -quality {quality} "{outpath}"'
        
        try:
            subprocess.run(cmd, shell=True, check=True)
            return  # Conversion succeeded, exit the loop
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e}")
        except FileNotFoundError:
            print("The 'convert' command was not found. Make sure it's installed and in your PATH.")
        
        retries += 1
        print(f"Retrying conversion for {input_path} (Attempt {retries}/{MAX_RETRIES})")
        time.sleep(1)  # Add a small delay between retries

    print(f"Max retries reached for {input_path}. Conversion failed.")


def main():
    image_files = json.loads(sys.argv[1])
    # image_files = ["out/1.tif","out/1.png","out/1.jpg",]

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for img_file in image_files:
            input_path =  img_file
            outpath, format =os.path.splitext(input_path)
            # print(outpath)
            outpath= outpath+"_comp"+format
            depth=sys.argv[2]
           
            quality = sys.argv[3]
            # outpath = os.path.join(directory_name, file_name+sys.argv[1])
            # output_path = os.path.join(output_folder, img_file)
            future = executor.submit(convert_image, input_path,outpath,format, depth ,  quality )
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
