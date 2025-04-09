# image_rotator.py

from PIL import Image

# load
im = Image.open('myimage.png')

# display image size
print(im.size)

# rotate once (counterclockwise)
rotated = im.rotate(90)

# save
rotated.save('rotated.png')
