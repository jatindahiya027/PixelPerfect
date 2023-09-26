import torch
from utils import colorize
from PIL import Image
import sys
import matplotlib.pyplot as plt
import os
# import torch_directml
def predict_depth(image):
    # device = torch_directml.device(torch_directml.default_device())
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    # DEVICE = device
    model = torch.hub.load('isl-org/ZoeDepth', "ZoeD_NK", pretrained=True).to(DEVICE).eval()
    depth = model.infer_pil(image)
    return depth

def main(input_image_path, output_depth_path):
    input_image = Image.open(input_image_path).convert('RGB')
    depth = predict_depth(input_image)

    # Colorize depth map
    colored_depth = colorize(depth, cmap='gray_r')
    # Convert the NumPy array to a PIL Image
    colored_depth_image = Image.fromarray((colored_depth * 255).astype('uint8'))
    
    # Get the dimensions (height and width) of the input image
    input_image_width, input_image_height = input_image.size

    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(input_image_width/100, input_image_height/100), dpi=130)

    # Display the colored depth image
    ax.imshow(colored_depth, cmap='gray_r')

    # Optionally, you can remove the axis labels and ticks if you prefer
    ax.axis('off')

    plt.savefig(output_depth_path, bbox_inches='tight', pad_inches=0)

    # Close the Matplotlib figure to release resources
    plt.close()
   
    image = Image.open(output_depth_path)

        # Resize the image to the desired width and height
    resized_image = image.resize((input_image_width, input_image_height))

        # Save the resized image to the output path
    resized_image.save(output_depth_path)

   

if __name__ == '__main__':
    input_image_path = sys.argv[1]   # Replace with your input image path
    # output_depth_path = sys.argv[2] 
    directory, full_filename = os.path.split(input_image_path)
    filename, extension = os.path.splitext(full_filename)
    output = directory+"/"+filename+"_depth.jpg"
    main(input_image_path, output)