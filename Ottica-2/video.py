import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.ndimage.measurements import center_of_mass as cm
from scipy.signal import savgol_filter as sf

def distanzaMedia(immagine,media):
	Min=immagine.min()
	d=0
	immagine=immagine-Min
	for i in range(len(immagine)):
		for j in range(len(immagine[0])):
			d+=np.sqrt(immagine[i][j]*((media[1]-i)**2+(media[0]-j)**2))
	return d/immagine.sum()

f=open('dati/distanza_media.txt','w+')
cm1=np.transpose(np.genfromtxt('dati/centro_di_massa.txt',unpack='True'))
for i in range(5):
	img=mpimg.imread('dati/fotogrammi/'+str(i)+'.jpg')[:,:,0]
	d=distanzaMedia(img,cm1[i])
	print(d,file=f)
	print(i)
	plt.imshow(img)
	plt.errorbar(cm1[i][1],cm1[i][0],yerr=d,xerr=d,color='purple')
	plt.savefig('immagini/video/'+str(i)+'.png')
	plt.close()
f.close()