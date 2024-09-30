import os
import shutil

src_dir = '/content/drive/MyDrive/I2T Recognition Dataset/ships_images'
filesplit_dirs = [
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/1',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/2',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/3',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/4',
    '/content/drive/MyDrive/I2T Recognition Dataset/ships_images/5'
]

for dir in filesplit_dirs: 
    os.makedirs(dir, exist_ok=True)
image_files = os.listdir(source_dir)

dir_num = 0

for image_file in image_files:
    if image_file.endswith(('.png', '.jpg', '.jpeg')):
        src = os.path.join(src_dir, image_file)
        detect_dir = filesplit_dirs[dir_num]
        file_path = os.path.join(detect_dir, image_file)
        shutil.move(src, file_path)
        dir_num += 1
        if dir_num >= len(filesplit_dirs):
            dir_num = 0
