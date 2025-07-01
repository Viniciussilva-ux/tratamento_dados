import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar os primeiros registros
print(df.head().to_string())
print(df.tail().to_string())

# Verificar a quantidade de linhas e colunas
print('Qtd:', df.shape)

# Verificar os tipos de dados
print('Tipagem:\n', df.dtypes)

# Checar valores nulos
print('Valores nulos:\n', df.isnull().sum())
