import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image

def calculate_aspect_ratio(width, height):
    return width / height

def count_colors(image):
    # Convert the image to RGB mode if it's not already
    image = image.convert('RGB')
    # Get the histogram of the image
    hist = image.histogram()
    # Calculate the number of non-zero entries in the histogram
    num_colors = sum(1 for count in hist if count != 0)
    return num_colors

def calculate_image_entropy(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray_image], [0], None, [256], [0,256])
    hist /= hist.sum()
    entropy = -np.sum(hist * np.log2(hist + 1e-10))
    return entropy

def calculate_color_distribution(image):
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = hist.flatten()
    return hist / hist.sum()

def calculate_texture_features(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = cv2.calcHist([gray_image], [0], None, [256], [0,256])
    glcm = glcm / glcm.sum()
    return glcm

def extract_image_features(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to RGB mode
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get image dimensions
    height, width, _ = image.shape
    
    # Calculate aspect ratio
    aspect_ratio = calculate_aspect_ratio(width, height)

    # Convert the image to PIL format
    pil_image = Image.fromarray(image)

    # Present colors
    color_count = count_colors(pil_image)

    # Calculate image entropy
    entropy = calculate_image_entropy(image)
    
    # Calculate color distribution
    color_distribution = calculate_color_distribution(image)
    
    # Calculate texture features
    texture_features = calculate_texture_features(image)
    
    return {
        'Image': os.path.basename(image_path),
        'Width': width,
        'Height': height,
        'Aspect Ratio': aspect_ratio,
        'Colors': color_count,
        'Entropy': entropy,
        'Color Distribution': color_distribution.tolist(),
        'Texture Features': texture_features.tolist()
    }

def process_images_in_folder(folder_path):
    image_features_list = []
    
    # Iterate over each image file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(folder_path, filename)
            image_features = extract_image_features(image_path)
            image_features_list.append(image_features)
    
    # Create a DataFrame from the list of image features
    df = pd.DataFrame(image_features_list)
    return df

# Folder containing images
folder_path = 'original'

# Process images in the folder and create a DataFrame
image_df = process_images_in_folder(folder_path)

image_df.to_csv('pixelizer_extended.csv', index=False)
# Display the DataFrame
print(image_df)
