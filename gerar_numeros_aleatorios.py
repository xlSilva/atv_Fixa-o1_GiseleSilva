# gerar_numeros_aleatorios
import numpy as np

np.random.seed(5)
matrix_original = np.random.rand(4,4)
# matrix = np.array(matrix_original*100*100, dtype=int) / 100
matrix = np.trunc(matrix_original*100*100) / 100

np.savetxt("dados.txt", matrix)
