from PIL import Image

img = Image.open('jaba.jpeg')
img.show()
width, height = img.size
print("Размер изображения: {}x{}".format(width, height))
print("Формат файла: {}".format(img.format))
print("Цветовая модель: {}".format(img.mode))


