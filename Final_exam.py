
# coding: utf-8

# In[ ]:


Question 2


# In[3]:


class myobj:
    def __init__(self, name):
        self.dependencies = []
        self.name = name

    def add_dependency(self, *myobj):
        self.dependencies.extend(myobj)

    def build(self, names=None):
        if names is None:
            names = []

        for i in self.dependencies:
            if i.name not in names:
                i.build(names)
                names.append(i.name)

        return names

    def __str__(self):
        return self.name
    
luke    = myobj("Luke")
hansolo = myobj("Han Solo")
leia    = myobj("Leia")
yoda    = myobj("Yoda")
padme   = myobj("Padme Amidala")
anakin  = myobj("Anakin Skywalker")
obi     = myobj("Obi-Wan")
darth   = myobj("Darth Vader")
_all    = myobj("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()


# In[ ]:


Question 1


# In[17]:


import numpy as np

class polynomial(object):
    def __init__(self, c, v='x'):
        self.coeff = c
        self.v = v
    def __repr__(self):
        coeff = self.coeff
        v = self.v
        s = ''
        D = len(coeff)
        
        first = True
        
        for i in range(D):
            pw = D-i-1
            pre = '+' if coeff[i]>0 else ''

            if first:
                if pre=='+':
                    pre = ''
                first = False
            
            if pw == 0:
                vname = ''
            elif pw == 1:
                vname = 'sin(' + v + ')'
            elif pw == D-1:
                vname = 'cos(' + str(D-1) + v + ')'
            else:
                vname = 'sin(' + str(pw) + '' + v + ')'

            if coeff[i] != 0:
                s += pre+str(coeff[i])+ vname + ' '
               
        return s
    def __add__(self,b):
        L_a = len(self.coeff)
        L_b = len(b.coeff)
        
        coeff = self.coeff if L_a > L_b else b.coeff
        short = self.coeff if L_a <= L_b else b.coeff
        
        for i in range(len(short)):
            coeff[-1-i] += short[-1-i]
            
        return polynomial(coeff, self.v)

p = polynomial([3, 7.1, 0.3, -3], 'x')
print(p)

