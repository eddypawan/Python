import os
from PIL import Image, ImageEnhance
from tqdm import tqdm

def upscale_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of files in the input folder
    files = os.listdir(input_folder)

    # Create a progress bar for the files
    progress_bar = tqdm(files, desc="Upscaling Images")

    # Iterate over the files in the input folder
    for file in progress_bar:
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        # Open the input image
        image = Image.open(input_path)

        # Upscale the image by 4x using the nearest-neighbor interpolation
        upscaled_image = image.resize((image.width * 4, image.height * 4), resample=Image.NEAREST)

        # Apply image quality improvements
        enhancer = ImageEnhance.Sharpness(upscaled_image)
        sharpness_factor = 2.0  # Increase the sharpness factor (adjust as needed)
        improved_image = enhancer.enhance(sharpness_factor)

        # Save the upscaled and improved image
        improved_image.save(output_path)

        # Update the progress bar with the current file name
        progress_bar.set_postfix(file=file)

# Example usage
input_folder = "G:/Python/pythonRepo/Python/Files/tobeupscaleImages"
output_folder = "G:/Python/pythonRepo/Python/Files/upscaledImages"

upscale_images(input_folder, output_folder)
