import os

def rename_images(directory):
    # Check if the provided path is a directory
    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return

    files = os.listdir(directory)

    # Filter only image files
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

    image_files.sort()

    # Rename each image in the directory with in an incrementing order
    for index, old_name in enumerate(image_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"{index}{extension}"
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

if __name__ == "__main__":
    # Example usage: replace 'original' with your actual path 
    directory_path = 'original'
    rename_images(directory_path)
