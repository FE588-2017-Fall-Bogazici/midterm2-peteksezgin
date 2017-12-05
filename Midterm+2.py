
# coding: utf-8

# In[8]:

import numpy as np
class polynomial(object):
    def __init__(self, c, v):
        self.coeff = c
        self.v = v
    def __repr__(self):
        D = len(self.coeff)
        for i in range(D):
            if i<D-1:
                print(self.coeff[i], end='')
                print('{}^{} '.format(self.v, D-i-1), end='')
            else:
                print(self.coeff[i])
        
        return str(self.coeff)
    
    def __add__(self,b):
        """Computes a+b and returns the result"""
        ### Note:  This code does not add polynomials 
        ###        of different orders so you must fix this
        D = len(self.coeff)
        if len(self.coeff)>len(b.coeff):
            for i in range(len(self.coeff)-len(b.coeff)):
                b.coeff.insert(0,0)
    
        else:
            for i in range(abs(len(self.coeff)-len(b.coeff))):
                   self.coeff.insert(0,0)
        coeff = []
        for i in range(max(D,len(b.coeff))):
            coeff.append(self.coeff[i] + b.coeff[i])
        return polynomial(coeff, self.v)
    
    def __sub__(self,b):
        
        """Computes a-b and returns the result"""
        
        D = len(self.coeff)
        if len(self.coeff)>len(b.coeff):
            for i in range(len(self.coeff)-len(b.coeff)):
                b.coeff.insert(0,0)
    
        else:
            for i in range(abs(len(self.coeff)-len(b.coeff))):
                   self.coeff.insert(0,0)
        coeff = []
        for i in range(max(D,len(b.coeff))):
            coeff.append(self.coeff[i] - b.coeff[i])
        return polynomial(coeff, self.v)
    
    
    def __mul__(self,b):
        """Computes a*b and returns the result"""

        coeff = np.convolve(self.coeff,b.coeff)
        print(coeff)
        return polynomial(coeff, self.v)
    
get_ipython().magic('matplotlib inline')
import matplotlib.pylab as plt
x=np.random.randn(100)
y1=x**2+6*x+7
plt.plot(y1,x)
y2=x**2-2*x-1
plt.plot(y2,x)
y3=8*x+12
plt.plot(y3,x)

            
p = polynomial([2,3,1], 'z')
print(p)

q = polynomial([0,4,4], 'z')
# Your program must also work when we define more naturally
# q = polynomial([4,4], 'z')
print(q)

print('--------------------')
print('Result of p + q:')
r1 = p + q
print(r1)

print('--------------------')
print('Result of p - q:')
r2 = p - q
print(r2)

print('--------------------')
print('Result of p * q:')
r3 = p * q
print(r3)

print('--------------------')
# Generates a plot
plt.show()


# In[ ]:



