import os
from PIL import Image

def is_image_corrupted(file_path):
    try:
        with Image.open(file_path) as img:
            # Try to load the image data
            img.load()
            return False  # Image is not corrupted
    except Exception as e:
        # Image loading failed indicating it's a corrupted file
        print(f"Error loading image '{file_path}': {e}")
        return True  # Image is corrupted

def detect_corrupted_images(folder_path):
    corrupted_images = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            if is_image_corrupted(file_path):
                corrupted_images.append(file_name)
    return corrupted_images


folder_path = "path/to/your/folder"  # Replace with the path to your folder containing images
corrupted_images = detect_corrupted_images(folder_path)
if corrupted_images:
    print("Corrupted images:")
    for image_name in corrupted_images:
        print(image_name)
else:
    print("No corrupted images found in the folder.")
