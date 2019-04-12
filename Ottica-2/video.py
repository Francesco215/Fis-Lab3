import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


img=mpimg.imread('dati/fotogrammi/4.jpg')
imgplot=plt.imshow(img)
lum_img=img[:,:,0]
