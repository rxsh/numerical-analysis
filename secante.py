import numpy as np

def f(x):
    return x-0.5*np.tan(x)

x0 = 1
x1 = 1.5

for i in range(10):
    x2 = x1 - (f(x1)*(x1 - x0))/(f(x1)-f(x0))
    x0 = x1
    x1 = x2
    print(f"Iteracion: {i+1}\tR: {x2}")