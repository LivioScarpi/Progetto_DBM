from PIL import Image
from numpy import asarray
import numpy as np

# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot

# load the image
image = Image.open('./olivetti_PNG_master/images/image-0.png')
# convert image to numpy array
data = asarray(image)

print("STAMPO IL NUMPY ARRAY")
print(data)

print("STAMPO IL TIPO DI NUMPY ARRAY")
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(" ", image2.mode)
print(image2.size)


# display the array of pixels as an image
# il parametro cmap serve a specificare il tipo di colormap che vogliamo utilizzare, per questo motivo abbiamo specificato gray per la scala di grigi
# pyplot.imshow(image, cmap='gray')
# pyplot.show()

im = np.array(image.convert('L')) #you can pass multiple arguments in single line
print("SONO QUA 1")

print(type(im))

# gr_im= Image.fromarray(im).save('gr_kolala.png')

print("SONO QUA 2")

grey_levels = 256

# Define the window size
windowsize_r = 8
windowsize_c = 8

# Crop out the window and calculate the histogram
for r in range(0,data.shape[0] - windowsize_r, windowsize_r):
    for c in range(0,data.shape[1] - windowsize_c, windowsize_c):
        window = data[r:r+windowsize_r,c:c+windowsize_c]
        hist = np.histogram(window,bins=grey_levels)
        print(window)
        imagetest = Image.fromarray(window)
        # pyplot.imshow(imagetest, cmap='gray')
        # pyplot.show()


