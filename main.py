from time import sleep
from funcoes import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dados/dados_indicium.csv")
df["nome"].fillna("indefinido", inplace=True)
df["host_name"].fillna("sem nome", inplace=True)
df["reviews_por_mes"].fillna(0, inplace=True)
df["ultima_review"].fillna(0, inplace=True)

while True:
    print()
    print("0 - Sair.")
    print("1 - Gráfico com frequência da coluna escolhida.")
    print("2 - Verificar tipos de dados do data frame.")
    print("3 - Gráfico Boxplot da coluna escolhida.")
    print("4 - Exibir correlação entre as colunas.")
    print()

    opcao = str(input("Digite a opção desejada: "))

    if opcao == "0":
        print("Saindo...")
        sleep(1)
        break

    elif opcao == "1":
        coluna = input_coluna()
        grafico_frequancia(df, coluna)

    elif opcao == "2":
        print()
        print(df.dtypes)
        print()

    elif opcao == "3":
        coluna = input_coluna()
        grafico_boxplot(df, coluna)

    elif opcao == "4":
        mapa_correlacao(df)
