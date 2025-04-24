import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: x**3 + 4*x**2 - 10
x0 = 1
x1 = 2
# tol = 0.0000001

tramo = x1 - x0
iteracion = 1  # Contador de iteraciones

while (iteracion < 20):
    x2 = (x0 + x1) / 2
    fa = fx(x0)
    fb = fx(x1)
    fc = fx(x2)

    cambia = np.sign(fa) * np.sign(fc)
    if cambia < 0:
        x1 = x2
    elif cambia > 0:
        x0 = x2

    tramo = x1 - x0

    # Imprimir la iteración y el valor actual de la raíz aproximada
    print(f"Iteración: {iteracion}\tR: {x2}")
    iteracion += 1

print('La raíz es: ', x2)
# print('Error en tramo: ', tramo)