import os
from PIL import Image

def upscale_images(input_folder, output_folder, scale_factor):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get the list of files in the input folder
    files = os.listdir(input_folder)
    
    # Iterate over the files in the input folder
    for file in files:
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)
        
        # Open the input image
        image = Image.open(input_path)
        
        # Calculate the new size based on the scale factor
        width = int(image.width * scale_factor)
        height = int(image.height * scale_factor)
        
        # Upscale the image using the 'Lanczos' resampling method
        upscaled_image = image.resize((width, height), Image.LANCZOS)
        
        # Save the upscaled image
        upscaled_image.save(output_path)

# Example usage
input_folder = "G:/Python/pythonRepo/Python/Files/tobeupscaleImages"
output_folder = "G:/Python/pythonRepo/Python/Files/upscaledImages"
scale_factor = 2  # Increase the image size by a factor of 2

upscale_images(input_folder, output_folder, scale_factor)
