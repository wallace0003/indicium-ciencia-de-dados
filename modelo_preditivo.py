import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("dados/dados_indicium.csv")

df["nome"] = df["nome"].fillna("indefinido")
df["host_name"] = df["host_name"].fillna("sem nome")
df["reviews_por_mes"] = df["reviews_por_mes"].fillna(0)
df["ultima_review"] = df["ultima_review"].fillna(0)


encoder = OneHotEncoder(drop='first')
encoded_features = encoder.fit_transform(df[['bairro_group', 'room_type']]).toarray()  # Convertendo para array denso
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(['bairro_group', 'room_type']))


X = pd.concat([encoded_df, df[['minimo_noites', 'numero_de_reviews', 'disponibilidade_365']]], axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
rmse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")


apartamento = {
    'id': 2595,
    'nome': 'Skylit Midtown Castle',
    'host_id': 2845,
    'host_name': 'Jennifer',
    'bairro_group': 'Manhattan',
    'bairro': 'Midtown',
    'latitude': 40.75362,
    'longitude': -73.98377,
    'room_type': 'Entire home/apt',
    'minimo_noites': 1,
    'numero_de_reviews': 45,
    'ultima_review': '2019-05-21',
    'reviews_por_mes': 0.38,
    'calculado_host_listings_count': 2,
    'disponibilidade_365': 355
}


apartamento_df = pd.DataFrame([apartamento])


encoded_apartamento = encoder.transform(apartamento_df[['bairro_group', 'room_type']]).toarray()
encoded_apartamento_df = pd.DataFrame(encoded_apartamento, 
            columns=encoder.get_feature_names_out(['bairro_group', 'room_type']))


X_apartamento = pd.concat([encoded_apartamento_df, apartamento_df[['minimo_noites', 
        'numero_de_reviews', 'disponibilidade_365']]], axis=1)


preco_previsto = modelo.predict(X_apartamento)


print(f"Preço previsto para o apartamento: ${preco_previsto[0]:.2f}")







