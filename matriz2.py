import numpy as np

def matrix2(n):
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):

            if i>j:
                # debajo de la diagonal
                A[i,j] = (i+1) * (j+1)
            else:
                # encima de la diagonal 
                A[i,j] = -(i+1) * (j+1)

    return A

M = matrix2(5)
print("Matriz M: \n", M)

# (np.linalg.inv(B-np.eye(5)))@B@A@(np.linalg.inv(B))