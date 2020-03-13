
from dft import dft
from numpy import loadtxt
from pylab import plot, show

data = loadtxt('pitch.txt',float)

mydft=dft()

a=mydft.dft(data[:,3])
b=list(map(abs,a))

plot(b)
show()

