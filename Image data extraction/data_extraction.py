from PIL import Image
import pandas as pd

def count_colors(image):
    # Convert the image to RGB mode if it's not already
    image = image.convert('RGB')
    # Get the histogram of the image
    hist = image.histogram()
    # Calculate the number of non-zero entries in the histogram
    num_colors = sum(1 for count in hist if count != 0)
    return num_colors


def process_image(image_path):
    with Image.open(image_path) as img:
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        print(image_name)
        width, height = img.size
        aspect_ratio = width / height
        colors = count_colors(img)
    return {'Image': image_name, 'Width': width, 'Height': height, 'Aspect Ratio': aspect_ratio, 'Colors': colors}

def create_dataframe(folder_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            data.append(process_image(image_path))
    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    folder_path = 'original' # Path to your images
    df = create_dataframe(folder_path)
    df.to_csv('pixelizer.csv', index=False) # .csv file name
    print(df)
