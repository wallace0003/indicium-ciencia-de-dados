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
    print("5 - dados estatísticos de determinada coluna")
    print("6 - Boxplot de distribuição do preço pela coluna desejada.")
    print("7 - grafico de dispersão da coluna deseja em comparação com o preço.")
    print("8 - Gráfico de relação entre preço médio e demanda por bairro.")
    print("9 - Criação de gráfico de linha da coluna desejada pelo preço médio")
    print("10 - indentificar correlação entre duas variáveis.")
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

    elif opcao == "5":
        coluna = input_coluna()
        estatisticas_coluna(df, coluna)

    elif opcao == "6":
        coluna = input_coluna()
        boxplot_com_preco(df, coluna)

    elif opcao == "7":
        coluna = input_coluna()
        grafico_dispersao_preco(df, coluna)

    elif opcao == "8":
        preco_demanda = df.groupby('bairro_group').agg(
            {'price': 'mean', 'numero_de_reviews': 'sum'}).reset_index()
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='price', y='numero_de_reviews', hue='bairro_group', data=preco_demanda, s=100)
        plt.title("Relação entre Preço Médio e Demanda por Bairro")
        plt.xlabel("Preço Médio")
        plt.ylabel("Número Total de Reviews")
        plt.legend(title="Grupo de Bairro")
        plt.show()
    
    elif opcao == "9":
        coluna = input_coluna()
        grafico_linha_preco_medio(df, coluna)

    elif opcao == "10":
        coluna1 = input_coluna()
        coluna2 = input_coluna()
        correlacao = df[[coluna1, coluna2]].corr()
        print("Correlação:")
        print()
        print(correlacao)
        print()
