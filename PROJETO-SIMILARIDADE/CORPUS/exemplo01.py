import pandas as pd
import numpy as np

#Para que possa ser armazenado as coleções de texto dentro do programa, criar váriavel que é um array
#Criação da coleção de dados
textos = ["O rato roeu a roupa do rei de Roma.","Vagabundo tem em todo lugar!","A situação faz o sapo pular","Não gostou, processa!","Você é um moleque","O rato roeu o processo do vagabundo. Se fosse na minha empresa, você já estava fora!"]
 
 #Rótulos atribuídos a cada texto armazenado dentro do corpus
classes = ["S1MP5ON", "LANCHES", "LANCHES", "S1MP5ON", "S1MP5ON", "LANCHES"]

#Criar a estrutura para armazenamento dos textos e classes (DataFrame)
df = pd.DataFrame({'textos':textos, 'classes':classes})

#Imprime o formato em que os dados são armazenados dentro do DataFrame
print(df)
#A primeira coluna sempre representa o id, que é o identificador.