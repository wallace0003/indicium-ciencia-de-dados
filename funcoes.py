import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from time import sleep


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