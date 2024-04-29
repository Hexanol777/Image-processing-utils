import os
from PIL import Image

def resize_images_in_folder(folder_path, output_folder, size):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    for root, dirs, files in os.walk(folder_path):
        for file in files:

            if file.endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)

                with Image.open(file_path) as img:
                    img_resized = img.resize(size)
                    relative_path = os.path.relpath(file_path, folder_path)
                    output_path = os.path.join(output_folder, relative_path)
                    output_dir = os.path.dirname(output_path)

                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                    img_resized.save(output_path)

def main():
    input_folders = input("Enter the paths of the folders (separated by spaces): ").split()
    output_folder = input("Enter the output folder path: ")
    width = int(input("Enter the width for resizing: "))
    height = int(input("Enter the height for resizing: "))
    size = (width, height)

    for folder_path in input_folders:
        resize_images_in_folder(folder_path, output_folder, size)

    print(f"Images resized and saved in the {output_folder}.")

if __name__ == "__main__":
    main()
