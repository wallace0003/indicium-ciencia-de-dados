import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from time import sleep
import pandas as pd

def grafico_frequancia(df, coluna:str):
    try:
        df[coluna].hist(bins=50)
        plt.title("Distribuição: " + coluna)
        plt.xlabel("Valores")
        plt.ylabel("Frequência")
        plt.axvline(df[coluna].mean(), color='red', linestyle='dashed', linewidth=1.4, label="Média")
        plt.axvline(df[coluna].median(), color='black', linestyle='dashed', linewidth=1.4, label="Mediana")
        plt.legend()
        plt.show()
    except KeyError:
        print()
        print("Essa coluna não existe!")
        sleep(1)
    except:
        print("Essa coluna não existe ou não é numérica!")
        sleep(1)

def grafico_boxplot(df, coluna:str):
    try:
        sns.boxplot(x=df[coluna])
        plt.title("Boxplot: " + coluna )
        plt.show()
    except KeyError:
        print()
        print("Essa coluna não existe!")
        sleep(1)
    except:
        print("Essa coluna não existe ou não é numérica!")
        sleep(1)
    
def input_coluna():
    coluna = str(input("Digite a coluna que deseja analizar: "))
    return coluna

def mapa_correlacao(df):
    # Calcular a matriz de correlação
    correlacao = df.select_dtypes(include=['number']).corr()
    # Criar o heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlacao, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Mapa de Calor das Correlações")
    plt.show()

def estatisticas_coluna(df, coluna):
    if coluna not in df.columns:
        print(f"A coluna '{coluna}' não existe no DataFrame.")
        return
    
    if not pd.api.types.is_numeric_dtype(df[coluna]):
        print(f"A coluna '{coluna}' não é numérica.")
        return

    print(f"Estatísticas para a coluna: {coluna}\n")
    print(df[coluna].describe())
    print("\nMétricas individuais:")
    print(f"Média: {df[coluna].mean():.2f}")
    print(f"Mediana: {df[coluna].median():.2f}")
    print(f"Moda: {list(df[coluna].mode())}")
    print(f"Desvio Padrão: {df[coluna].std():.2f}")
    print(f"Variância: {df[coluna].var():.2f}")
    print(f"Valor Mínimo: {df[coluna].min()}")
    print(f"Valor Máximo: {df[coluna].max()}")
    print(f"Percentil 25%: {df[coluna].quantile(0.25):.2f}")
    print(f"Percentil 75%: {df[coluna].quantile(0.75):.2f}")

def boxplot_com_preco(df, coluna):
    plt.figure(figsize=(12,6))
    sns.boxplot(x=coluna, y='price', data=df)
    plt.xticks(rotation=90) 
    plt.title("Distribuição dos Preços por " + coluna)
    plt.xlabel(coluna)
    plt.ylabel("Preço")
    plt.show()

def grafico_dispersao_preco(df, coluna):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[coluna], y=df["price"], alpha=0.5)
    plt.title("Relação entre Número de " + coluna + " e Preço")
    plt.xlabel("Número " + coluna)
    plt.ylabel("Preço")
    plt.show()

