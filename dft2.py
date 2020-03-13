
m numpy import zeros,loadtxt
from pylab import plot,xlim,show
from cmath import exp,pi

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
	x[n]=
        c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

y = loadtxt("co2_mm_gl.txt",float)
#a = (y[:,4])
c=dft(y[:,4])
plot(abs(c))
show()


