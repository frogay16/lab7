from PIL import Image


img = Image.open("jaba.jpeg")
width, height = img.size


new = (int(width/3), int(height/3))
small = img.resize(new)
small.save("mini_jaba.jpg")


mirror_img_h = small.transpose(Image.FLIP_LEFT_RIGHT)
mirror_img_v = small.transpose(Image.FLIP_TOP_BOTTOM)

mirror_img_h.save("mirror_hor_jaba.jpg")
mirror_img_v.save("mirror_vert_jaba.jpg")
