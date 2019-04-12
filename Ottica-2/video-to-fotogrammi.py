import cv2

vidcap=cv2.VideoCapture('dati/interferenza.mp4')

conteggio=0
successo,immagine=vidcap.read()
while successo:
	successo,imaggine=vidcap.read()
	cv2.imwrite("dati/fotogrammi/%d.jpg" % conteggio, imaggine)
	if cv2.waitKey(10)==27: break
	conteggio=conteggio+1