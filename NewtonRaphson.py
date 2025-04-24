import numpy as np

f = lambda x: x**2 - 5*x + 6

def derivada(f, x, h=0.0001):
    return (f(x + h) - f(x))/h

x = 5 # initial point
print(f"x0 = {x}")

for i in range(10):
    fx = f(x)
    dfx = derivada(f,x) # usar la derivada númerica
    x = x - fx/dfx # actualiza la aproximación
    print(f"{i+1} = {x}") # resultado