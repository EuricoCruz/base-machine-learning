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

#Separa dados de treino e de teste
treino_dados = X[:tamanho_do_treino]
treino_marcacoes = Y[:tamanho_do_treino]
teste_dados = X[-tamanho_do_teste:]
teste_marcacoes = Y[-tamanho_do_teste:]


from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)
resultado = modelo.predict(teste_dados)
acertos = resultado == teste_marcacoes
total_de_acertos = sum(acertos)
total_dos_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_dos_elementos

# a eficácia do algoritmo que chuta tudo 0 ou 1
acerto_de_um =  len(Y[Y=='sim'])
acerto_de_zero = len(Y[Y=='nao'])
taxa_de_acertos_base = 100.0 * max(acerto_de_um, acerto_de_zero)


print("Total de acertos do algoritmo base: %f" % taxa_de_acertos_base)
print("Total de acertos do algoritmo: %f" % taxa_de_acerto)
print(total_dos_elementos)
