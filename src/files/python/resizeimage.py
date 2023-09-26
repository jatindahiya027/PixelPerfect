import subprocess
import sys
import os
import concurrent.futures
# from PIL import Image
import time
import subprocess
import sys
import json
MAX_RETRIES = 20
def resize_with_aspect_ratio(input_path, output_path, new_width, new_height,mode):
    # Construct the ImageMagick command for aspect ratio-preserving resize
    
    retries = 0
    while retries < MAX_RETRIES:
        if mode=="1":
            cmd = f'convert "{input_path}" -resize {new_width}x{new_height}^ -gravity center  "{output_path}"'  
        else:
            cmd =f'convert "{input_path}" -resize {new_width}x{new_height}! "{output_path}"'
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


if __name__ == "__main__":
    
    # Example usage:
    image_files = json.loads(sys.argv[1])
    # image_files = ["out/1.png","out/1.jpg","out/2.jpg","out/3.png","out/4.png","out/5.png","out/6.png","out/7.png"]
    
    new_width = sys.argv[2]
    new_height = sys.argv[3]
    mode = sys.argv[4]
    # resize_with_aspect_ratio(input_image_path, output_image_path, new_width, new_height)
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for img_file in image_files:
            input_path =  img_file
            outpath, format =os.path.splitext(input_path)
            # print(outpath)
            outpath= outpath+"_resize"+format

            future = executor.submit(resize_with_aspect_ratio, input_path,outpath, new_width, new_height,mode )
            futures.append(future)
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken: {elapsed_time:.2f} seconds")

