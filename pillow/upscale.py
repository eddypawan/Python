import os
from PIL import Image
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

        # Get the size of the image in bytes
        image_size = os.path.getsize(input_path)

        # Set the scale factor based on the image size
        if image_size < 2 * 1024 * 1024 and image_size > 1.5 * 1024 * 1024:
            scale_factor = 3
        elif image_size < 1.5 * 1024 * 1024:
            scale_factor = 4
        else:
            scale_factor = 2

        # Calculate the new size based on the scale factor ///review
        width = int(image.width * scale_factor)
        height = int(image.height * scale_factor)

        # Upscale the image using the 'Lanczos' resampling method
        upscaled_image = image.resize((width, height), Image.LANCZOS)

        # Save the upscaled image
        upscaled_image.save(output_path)

        # Update the progress bar with the current file name
        progress_bar.set_postfix(file=file)

# Example usage
input_folder = "G:/Python/pythonRepo/Python/Files/tobeupscaleImages"
output_folder = "G:/Python/pythonRepo/Python/Files/upscaledImages"

upscale_images(input_folder, output_folder)






