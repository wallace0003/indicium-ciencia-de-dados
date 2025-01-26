import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dados/dados_indicium.csv")

# Verificando quantas colunas tem valores nulos
print(df.isnull().sum())
#Substituindo valores nulos para melhor análise
df["nome"].fillna("indefinido", inplace=True)
df["host_name"].fillna("sem nome", inplace=True)
df["reviews_por_mes"].fillna(0, inplace=True)
df["ultima_review"].fillna(0, inplace=True)

print(df.isnull().sum())
print()
print(df.dtypes)