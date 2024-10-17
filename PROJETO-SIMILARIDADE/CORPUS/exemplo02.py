import pandas as pd

df = pd.read_csv(r'C:/Users/mayar/Downloads/6Semestre/PLN/exercicios/PROJETO-SIMILARIDADE/base.csv')

# Certifique-se de usar aspas para os nomes das colunas
data = pd.DataFrame({'Comentário': df['Comentario'], 'Avaliação': df['Avaliacao']})
print(data)
