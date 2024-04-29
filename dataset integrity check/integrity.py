from os import listdir
from os.path import isfile, join
import os
from PIL import Image
from tqdm.notebook import tqdm

images_path = 'original' # Path to your images folder
files = [f for f in listdir(images_path) if isfile(join(images_path, f))]

base_size = None
for file in tqdm(files):
  file2 = os.path.join(images_path,file)
  img = Image.open(file2)
  sz = img.size
  if base_size and sz!=base_size:
    print(f"Inconsistant size: {file2}")
  elif img.mode!='RGB':
    print(f"Inconsistant color format: {file2}")
  else:
    base_size = sz