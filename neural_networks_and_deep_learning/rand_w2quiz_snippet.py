import numpy as np

#Question 9
a = np.random.randn(3,3)
b = np.random.randn(3,1)
c = a*b

print(c, '\n')

#Question 5
g = np.random.randn(4, 3)
h = np.random.randn(4, 3)
i = g*h

print(i, '\n')

#Operands must have the same shape to be multiplied together
d = np.random.randn(4, 3)
e = np.random.randn(3, 2)
f = d*e

print(f)
