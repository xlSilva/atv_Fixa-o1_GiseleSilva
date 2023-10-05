import numpy as np

# Criar um array bidimensional com dados diferentes dos utilizados em sala;
# EXTRA (200XP): Os dados devem vir de algum arquivo externo.
matrix_data = np.genfromtxt("dados.txt",  delimiter =" ", dtype ="float64")
print(matrix_data)

# Obter dados estatísticos diferentes (pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis);
print(f" A média das colunas da matrix_data = {matrix_data.mean(axis=0)}")
print(f" A mediana da matrix_data = {np.median(matrix_data)}")
print(f" A soma dos elementos das linhas da matrix_data = {(matrix_data.sum(axis=1))}")


# Obter a transposta da matriz e realizar uma operação com ela;
matrix_transposta = matrix_data.T
print (f"A soma da matrix_data com sua transposta é {matrix_transposta + matrix_data}")

# Realizar um produto escalar entre duas matrizes ou de um array com uma matriz;
print(f'A multiplicação da matrix_data com a sua transposta é {matrix_data @ matrix_transposta}')

# Criar um filtro para a sua matriz;
index_maior = matrix_data[matrix_data > 90]
print(f'{matrix_data.argmax()}')

# Realizar alguma operação aritmética (número com matriz, array com matriz, etc.);
print(f"A multiplicação de um número por matriz é {matrix_data * 5} ")

# Vincular com o github (código deve estar no repositório sem o venv ou outros arquivos de configuração);
