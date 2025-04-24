import numpy as np
import matplotlib.pyplot as plt

# Nota: No existe una función directa para la cosecante en numpy.
# Sin embargo, puedes definirla como una función personalizada:
def csc(x):
    return 1 / np.sin(x)

def falsa_posicion(func, a, b, tol, max_iter):
    """
    Método de la Falsa Posición para encontrar raíces de una función.

    Parámetros:
    func: función a evaluar.
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    tol: tolerancia para el criterio de convergencia.
    max_iter: número máximo de iteraciones.

    Retorna:
    La raíz aproximada y el número de iteraciones realizadas.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("El intervalo no es válido. La función debe cambiar de signo en [a, b].")

    iteraciones = 0
    while iteraciones < max_iter:
        # Calcular el punto de falsa posición
        c = (a*func(b) - b*func(a)) / (func(b) - func(a))

        print(f"Iteración {iteraciones + 1}: c = {c}, f(c) = {func(c)}")

        # Verificar si c es una raíz o si la tolerancia se cumple
        if abs(func(c)) < tol or abs(b - a) < tol:
            return c, iteraciones

        # Actualizar los límites del intervalo
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

        iteraciones += 1

    raise RuntimeError("El método no convergió después del número máximo de iteraciones.")

if __name__ == "__main__":
    # Definir la función
    def f(x):
        return np.sin(x) - csc(x) + 1
    
    # Intervalo inicial
    a = 0.5
    b = 0.7

    # Parámetros del método
    tolerancia = 1e-6
    max_iteraciones = 100

    try:
        raiz, iteraciones = falsa_posicion(f, a, b, tolerancia, max_iteraciones)
        print(f"La raíz aproximada es: {raiz}")
        print(f"Número de iteraciones: {iteraciones}")
    except Exception as e:
        print(str(e))