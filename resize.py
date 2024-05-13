from PIL import Image
import os

def resize_and_crop(image_path, output_path, size):
    with Image.open(image_path) as img:
        # Resize the image without antialiasing
        resized_img = img.resize(size)
        
        # Crop the image if it's larger than the specified size
        cropped_img = resized_img.crop((0, 0, size[0], size[1]))
        
        # Save the cropped image
        cropped_img.save(output_path)

def resize_images():
    input_folder = 'memes'
    output_folder = 'memes'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_and_crop(image_path, output_path, (300, 300))  # Adjust the size as needed

if __name__ == "__main__":
    pass
