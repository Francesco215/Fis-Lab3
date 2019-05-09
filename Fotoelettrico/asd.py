import menzalib as mz
import numpy as np
def cifrat(x):
    i=0
    while (x-np.round(x,-i))!=0: i=i-1
    return i
cifra=np.vectorize(cifrat)


files=[450,499,545,577]
for i in range(len(files)):
	V,I =np.genfromtxt('dati/'+str(files[i])+'nm.txt',unpack=True)
	I=I*1e-12
	V=V*1e-3
	dV=mz.dVdig(V)
	dI=np.zeros(len(I))
	for j in range(len(I)):
		dI[j]=np.sqrt((I[j]*4e-3)**2+10.0**(cifra(I[j])*2))
		if I[j]==0: dI[j]=1e-13
	col1=mz.ne_tex(V*1000,dV*1000)
	col2=mz.ne_tex(I*1e12,dI*1e12)
	mz.mat_tex([col1,col2],titolo='$V[mV]$ & $I[pA]$')
