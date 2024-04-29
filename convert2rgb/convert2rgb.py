from PIL import Image
import os

def convert_to_rgb(folder_path):
    # a folder to save converted images if it doesn't exist
    output_folder = os.path.join(folder_path, 'rgb')
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        # Load image
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)

        # Convert to RGB if not already in RGB mode
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save the converted image
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)
        print(f"Converted {filename} to RGB and saved as {output_path}")

def main():
    # Folder containing images to convert
    folder_path = 'sprites'  # Replace with the path to your folder
    convert_to_rgb(folder_path)

if __name__ == "__main__":
    main()
