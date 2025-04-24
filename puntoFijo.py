import numpy as np

def punto_fijo(g, x0, tol, max_iter):
    """
    Método del Punto Fijo.
    
    Parámetros:
    g: función g(x) para la iteración.
    x0: valor inicial.
    tol: tolerancia para el criterio de convergencia.
    max_iter: número máximo de iteraciones.
    """
    iteraciones = 0
    x_actual = x0

    print(f"{'Iteración':<10}{'x':<20}{'Error':<20}")
    print("-" * 50)

    while iteraciones < max_iter:
        x_nuevo = g(x_actual)
        error = abs(x_nuevo - x_actual)
        print(f"{iteraciones:<10}{x_nuevo:<20.10f}{error:<20.10f}")

        if error < tol:
            print("\nConvergencia alcanzada.")
            return x_nuevo

        x_actual = x_nuevo
        iteraciones += 1

    print("\nNo se alcanzó la convergencia en el número máximo de iteraciones.")
    return x_actual

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la función g(x)
    g = lambda x: np.cos(x)  # Ejemplo: g(x) = cos(x)

    # Parámetros iniciales
    x0 = 0.5  # Valor inicial
    tol = 1e-6  # Tolerancia
    max_iter = 100  # Número máximo de iteraciones

    # Llamar al método del punto fijo
    resultado = punto_fijo(g, x0, tol, max_iter)
    print(f"\nResultado final: {resultado}")