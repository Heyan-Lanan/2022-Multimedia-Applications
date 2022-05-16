from PIL import Image
from pylab import *
import matplotlib.pyplot as plt
from skimage import io, data

# flower.jpg
im = array(Image.open('cat.jpg'))
im[:, :, 0] = im[:, :, 1] = im[:, :, 2] = (im[:, :, 0] * 0.3 + im[:, :, 1] * 0.59 + im[:, :, 2] * 0.11)
imshow(im)

imsave('./test2.jpg', im)
# img = data.chelsea()
# io.imshow(img)
# io.imsave('./cat.jpg', img)
# , './grey.jpg'
show()
