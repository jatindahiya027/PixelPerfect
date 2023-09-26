import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from SCUNet import SCUNet  # Assuming this is how you import the OmniSR class
import sys
import os



def vitogiff(input_image, output):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    # Load the pretrained model using the provided state_dict
    state_dict = torch.load(script_directory+'/scunet_color_real_psnr.pth', map_location='cpu')  # Load on CPU
    model = SCUNet(state_dict)
    if input_image.height >= 1800 or input_image.width >= 1800:
        # Split the image into 4 equal parts
    
        part_size = (input_image.width // 2, input_image.height // 2)
        parts = []

        for i in range(2):
            for j in range(2):
                left = i * part_size[0]
                upper = j * part_size[1]
                right = left + part_size[0]
                lower = upper + part_size[1]
                part = input_image.crop((left, upper, right, lower))
                parts.append(part)

        # Process each part and store the results
        super_resolved_parts = []

        for part in parts:
            # Define a transformation to prepare the image for the model
            preprocess = transforms.Compose([
                transforms.ToTensor(),  # Converts the image to a tensor
            ])
            print(part.size)
            # Apply the transformation to the input image
            input_image_tensor = preprocess(part).unsqueeze(0)  # Add batch dimension

            # Perform inference
            with torch.no_grad():
                super_resolved_image = model(input_image_tensor)

            # Convert the super-resolved tensor to a NumPy array
            super_resolved_image_numpy = super_resolved_image.squeeze(0).cpu().numpy()

            # Ensure values are in the [0, 255] range and convert to uint8 data type
            super_resolved_image_numpy = (super_resolved_image_numpy * 255).clip(0, 255).astype(np.uint8)

            # Create an RGB PIL Image from the NumPy array
            super_resolved_image_pil = Image.fromarray(super_resolved_image_numpy.transpose(1, 2, 0), 'RGB')
            super_resolved_parts.append(super_resolved_image_pil)

        temp = super_resolved_parts[1]
        super_resolved_parts[1]= super_resolved_parts[2]
        super_resolved_parts[2]= temp    

        # Calculate the dimensions of the final super-resolved image
        final_width = input_image.width 
        final_height = input_image.height 

        # Create a new image with the calculated dimensions
        final_super_resolved_image = Image.new('RGB', (final_width, final_height))

        # Paste the processed parts onto the new canvas
        x_offset = 0
        y_offset = 0
        for part in super_resolved_parts:
            final_super_resolved_image.paste(part, (x_offset, y_offset))
            x_offset += part.width
            if x_offset >= final_width:
                x_offset = 0
                y_offset += part.height

    else:
        # Define a transformation to prepare the image for the model
        preprocess = transforms.Compose([
            transforms.ToTensor(),  # Converts the image to a tensor
        ])

        # Apply the transformation to the input image
        input_image_tensor = preprocess(input_image).unsqueeze(0)  # Add batch dimension

        # Perform inference
        with torch.no_grad():
            super_resolved_image = model(input_image_tensor)

        # Convert the super-resolved tensor to a NumPy array
        super_resolved_image_numpy = super_resolved_image.squeeze(0).cpu().numpy()

        # Ensure values are in the [0, 255] range and convert to uint8 data type
        super_resolved_image_numpy = (super_resolved_image_numpy * 255).clip(0, 255).astype(np.uint8)

        # Create an RGB PIL Image from the NumPy array
        final_super_resolved_image = Image.fromarray(super_resolved_image_numpy.transpose(1, 2, 0), 'RGB')

    # Save the super-resolved image (replace 'output_image.jpg' with the desired output path)
    final_super_resolved_image.save(output)

if __name__ == "__main__":
    input_filename = sys.argv[1]  # Replace with your file name
    # type= sys.argv[2] 
    directory, full_filename = os.path.split(input_filename)
    filename, extension = os.path.splitext(full_filename)
    type = directory+"/"+filename+"_denoise"+extension
    input_filename = Image.open(input_filename)
    vitogiff(input_filename, type)