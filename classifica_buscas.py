import pandas as pd

dados = pd.read_csv("busca.csv")
X_df = dados[['home', 'busca', 'logado']]
Y_df = dados['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

percentual_de_treino = 0.9 
tamanho_do_treino = int(percentual_de_treino * len(X))
tamanho_do_teste = len(Y) - tamanho_do_treino

treino_dados = X[:tamanho_do_treino]
treino_marcacoes = Y[:tamanho_do_treino]
teste_dados = X[-tamanho_do_teste:]
teste_marcacoes = Y[-tamanho_do_teste:]


from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)
resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes
acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_dos_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_acertos

print(total_de_acertos)
print(total_dos_elementos)
