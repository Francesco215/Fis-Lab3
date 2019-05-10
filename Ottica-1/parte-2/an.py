import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 


zero = 168.63; dzero = 0.02
grad = np.array([225.07, 273.7])
dgrad = np.array([0.04,0.04])

rad_i = (np.pi - (grad[0]-zero)/57.32)/2; drad_i = dzero/(57.32*2)
rad_d = np.pi - rad_i - (grad - zero)/57.32; drad_d = (dgrad - dzero)/57.32
lamb = 546.074


def f(x,d):
	return np.sin(rad_i) - (x*lamb)/d

m = np.array([0,1]); dm = np.array([0,0])
m1 = np.array([-0.15, 0, 1, 1.15])

y = np.sin(rad_d); dy = np.abs(np.cos(rad_d)*drad_d)
err = (0.02*lamb)/((y[1] - y[0])**2)
print (err)
popt, pcov = curve_fit(f, m, y, sigma = dy, absolute_sigma = True)
print ("%g +- %g" % (popt, np.sqrt(pcov)))
plt.errorbar(m,y,dy,dm, linestyle='', color='red')
plt.plot(m1, f(m1, *popt), color='blue')
plt.xlabel(r'$m$')
plt.ylabel(r'$sin(\delta_{d})$')
plt.show()
