from google.colab import drive
import os
import shutil

drive.mount('/content/drive')

source_dir = '/content/drive/MyDrive/I2T Recognition Dataset/ships_images'
destination_dirs = [
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/1',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/2',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/3',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/4',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/5'
]

for dir in destination_dirs:
    os.makedirs(dir, exist_ok=True)

image_files = [f for f in os.listdir(source_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
num_dirs = len(destination_dirs)

for i, image_file in enumerate(image_files):
    src_path = os.path.join(source_dir, image_file)
    dest_dir = destination_dirs[i % num_dirs] 
    dest_path = os.path.join(dest_dir, image_file)
    shutil.move(src_path, dest_path)
    print(f'Moved {image_file} to {dest_dir}')

