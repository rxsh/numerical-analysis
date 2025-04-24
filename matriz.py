import numpy as np

def matriz_B(n):
    B = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i < j:
                B[i, j] = (-1)**(i+1) + j+1
            elif i == j:
                B[i,j] = (i+1) + (j+1)
            else:
                B[i,j] = (-1)**(j+1) + i+1
    
    return B

B = matriz_B(5)
print("Matriz B: \n", B)

(np.linalg.inv(B-np.eye(5)))@B