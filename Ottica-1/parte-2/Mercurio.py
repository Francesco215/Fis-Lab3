import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 


zero = 168.63; dzero = 0.02 #Angolo zero mercurio
grad = np.array([225.07, 273.7])
#Punto 225.07 modificato da 245.07 che aveva un angolo del reticolo di 76 gradi

dgrad = np.array([0.04,0.04])

rad_i = (np.pi - (grad[0]-zero)/57.32)/2; drad_i = dzero/(57.32*2)
rad_d = np.pi - rad_i - (grad - zero)/57.32; drad_d = (dgrad - dzero)/57.32
#Conversione grado-radiante

lamb = 546.074


def f(x,d):
	return np.sin(rad_i) - (x*lamb)/d

m = np.array([0,1]); dm = np.array([0,0])
m1 = np.array([-0.15, 0, 1, 1.15])

y = np.sin(rad_d); dy = np.abs(np.cos(rad_d)*drad_d)
<<<<<<< HEAD:Ottica-1/parte-2/an.py
err = (0.02*lamb)/((y[1] - y[0])**2)
print (err)
popt, pcov = curve_fit(f, m, y, sigma = dy, absolute_sigma = True)
print ("%g +- %g" % (popt, np.sqrt(pcov)))
=======

err = (0.02*lamb)/((y[1] - y[0])**2)   #<----- IGNORA QUESTO ERRORE E' UN ERRORE MOLTO FAKE E DI TEST.
print err #<----- IDEE SULLA STIMA DELL'ERRORE?

#Bellurie inutili e fit ancora più inutile con due punti che dio cane però quelli avevamo quindi Ok.
popt, pcov = curve_fit(f, m, y, sigma = dy, absolute_sigma = False)
print "%g +- %g" % (popt, np.sqrt(pcov))
>>>>>>> origin:Ottica-1/parte-2/Mercurio.py
plt.errorbar(m,y,dy,dm, linestyle='', color='red')
plt.plot(m1, f(m1, *popt), color='blue')
plt.xlabel(r'$m$')
plt.ylabel(r'$sin(\delta_{d})$')
plt.show()
