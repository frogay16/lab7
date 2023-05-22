from PIL import Image, ImageFilter
import os

img_folder = 'images'
new_folder = 'new_images'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for filename in os.listdir(img_folder):
    if filename.endswith('.jpeg'):
        img_path = os.path.join(img_folder, filename)
        img = Image.open(img_path)
        img_solarize = img.filter(ImageFilter.FIND_EDGES)

        new_filename = 'new_' + filename
        new_path = os.path.join(new_folder, new_filename)
        img_solarize.save(new_path)

print('Все изображения обработаны и сохранены в новую папку!')
